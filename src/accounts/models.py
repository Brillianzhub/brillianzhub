from django.core.validators import RegexValidator
from datetime import timedelta
from django.db import models
from django.urls import reverse
from django import forms
import random
from django.db.models import Q
from django.conf import settings
from django.utils import timezone
from django.contrib.auth.models import Group
from django.db.models.signals import pre_save, post_save
from django.contrib.auth.models import AbstractBaseUser, BaseUserManager, PermissionsMixin
from django.core.mail import send_mail
from django.template.loader import get_template
from brillianzhub.utils import random_string_generator, unique_key_generator, unique_id_referrer_generator

# Default email activation period in days
DEFAULT_ACTIVATION_DAYS = getattr(settings, 'DEFAULT_ACTIVATION_DAYS', 7)


def upload_image_path(instance, filename):
    new_filename = random.randint(1, 3910233549)
    name, ext = get_filename_ext(filename)
    final_filename = '{new_filename}{ext}'.format(
        new_filename=new_filename, ext=ext)
    return "users/{new_filename}/{final_filename}".format(
        new_filename=new_filename,
        final_filename=final_filename
    )


class UserManager(BaseUserManager):
    def create_user(self, email, password=None, is_active=True, is_admin=False, is_staff=False):
        if not email:
            raise ValueError("Please enter your email address")
        if not password:
            raise ValueError("Users must have a password")

        user_obj = self.model(
            email=self.normalize_email(email)
        )
        user_obj.set_password(password)
        user_obj.staff = is_staff
        user_obj.admin = is_admin
        user_obj.is_active = is_active
        user_obj.save(using=self._db)
        return user_obj

    def create_staffuser(self, email, password=None):
        user = self.create_user(
            email=email,
            password=password,
            is_staff=True,
        )
        return user

    def create_superuser(self, email, password=None):
        user = self.create_user(
            email=email,
            password=password,
            is_staff=True,
            is_admin=True,
            is_active=True,
        )
        return user

    def create_instructor(self, email, password=None):
        user = self.create_user(
            email=email,
            password=password,
            is_instructor=True
        )

        return user


class User(AbstractBaseUser, PermissionsMixin):
    email = models.EmailField(unique=True)
    is_active = models.BooleanField(default=True)
    active = models.BooleanField(default=True)
    instructor = models.BooleanField(default=False)
    staff = models.BooleanField(default=False)
    admin = models.BooleanField(default=False)
    timestamp = models.DateTimeField(auto_now_add=True)
    id_referrer = models.CharField(max_length=10, blank=True, null=True)

    USERNAME_FIELD = 'email'

    objects = UserManager()

    def __str__(self):
        return self.email

    def get_full_name(self):
        return self.email

    def get_short_name(self):
        return self.email

    def has_perm(self, perm, obj=None):
        return True

    def has_module_perms(self, app_label):
        return True

    @property
    def is_staff(self):
        return self.staff

    @property
    def is_admin(self):
        return self.admin

    @property
    def is_instructor(self):
        return self.instructor


def pre_save_create_id_referrer(sender, instance, *args, **kwargs):
    if not instance.id_referrer:
        instance.id_referrer = unique_id_referrer_generator(instance)


pre_save.connect(pre_save_create_id_referrer, sender=User)


class Profile(models.Model):
    user = models.OneToOneField(
        settings.AUTH_USER_MODEL, null=True, blank=True, on_delete=models.CASCADE)
    firstname = models.CharField(max_length=250)
    lastname = models.CharField(max_length=250)
    bios = models.TextField()
    date_of_birth = models.DateField(blank=True, null=True)
    country = models.CharField(max_length=250)
    contact = models.CharField(max_length=20)
    facebook_handle = models.CharField(
        max_length=30,
        validators=[
            RegexValidator(
                regex=r'^[A-Za-z0-9_.]+$',
                message='Facebook handle must be alphanumeric or contain underscores or periods.'
            ),
        ],
        blank=True,
        null=True
    )
    twitter_handle = models.CharField(
        max_length=15,
        validators=[
            RegexValidator(
                regex=r'^[A-Za-z0-9_]+$',
                message='Twitter handle must be alphanumeric or contain underscores.'
            ),
        ],
        blank=True,
        null=True
    )
    linkedin_handle = models.CharField(
        max_length=30,
        validators=[
            RegexValidator(
                regex=r'^[A-Za-z0-9_.-]+$',
                message='LinkedIn handle must be alphanumeric or contain underscores, periods, or hyphens.'
            ),
        ],
        blank=True,
        null=True
    )
    photo = models.ImageField(upload_to='users/%Y/%m/%d', blank=True)

    def __str__(self):
        return 'Profile for user {}'.format(self.user.profile.firstname)


class GroupExtend(models.Model):
    group = models.OneToOneField(Group, on_delete=models.CASCADE)


class Contact(models.Model):
    first_name = models.CharField(max_length=100)
    last_name = models.CharField(max_length=100)
    email_address = models.EmailField()
    subject = models.CharField(max_length=50)
    message = models.TextField()
    time = models.DateTimeField(auto_now_add=True, db_index=True)

    def __str__(self):
        return 'Message from {}'.format(self.email_address)


class EmailActivationQuerySet(models.query.QuerySet):
    def confirmable(self):
        now = timezone.now()
        start_range = now - timedelta(days=DEFAULT_ACTIVATION_DAYS)
        end_range = now
        return self.filter(
            activated=False,
            force_expired=False
        ).filter(
            timestamp__gt=start_range,
            timestamp__lte=end_range
        )


class EmailActivationManager(models.Manager):
    def get_queryset(self):
        return EmailActivationQuerySet(self.model, using=self._db)

    def confirmable(self):
        return self.get_queryset().confirmable()

    def email_exists(self, email):
        return self.get_queryset().filter(
            Q(email=email) |
            Q(user__email=email)
        ).filter(
            activated=False
        )


class EmailActivation(models.Model):
    user = models.ForeignKey(User, on_delete=models.CASCADE)
    email = models.EmailField()
    key = models.CharField(max_length=120, blank=True, null=True)
    activated = models.BooleanField(default=False)
    force_expired = models.BooleanField(default=False)
    expires = models.IntegerField(default=7)
    timestamp = models.DateTimeField(auto_now_add=True)
    update = models.DateTimeField(auto_now=True)

    objects = EmailActivationManager()

    def __str__(self):
        return self.email

    def can_activate(self):
        qs = EmailActivation.objects.filter(pk=self.pk).confirmable()
        if qs.exists():
            return True
        return False

    def activate(self):
        if self.can_activate():
            user = self.user
            user.is_active = True
            user.save()
            self.activated = True
            self.save()
            return True
        return False

    def regenerate(self):
        self.key = None
        self.save()
        if self.key is not None:
            return True
        return False

    def send_activation(self):
        if not self.activated and not self.force_expired:
            if self.key:
                base_url = getattr(settings, 'BASE_URL',
                                   'https://www.brillianzhub.com')
                key_path = reverse("accounts:email-activate",
                                   kwargs={'key': self.key})
                path = "{base}{path}".format(base=base_url, path=key_path)
                context = {
                    'path': path,
                    'email': self.email
                }
                txt_ = get_template(
                    "registration/emails/verify.txt").render(context)
                html_ = get_template(
                    "registration/emails/verify.html").render(context)
                subject = '1-Click Email Verification'
                from_email = settings.DEFAULT_FROM_EMAIL
                recipient_list = [self.email]

                sent_mail = send_mail(
                    subject,
                    txt_,
                    from_email,
                    recipient_list,
                    html_message=html_,
                    fail_silently=False,
                )
                return sent_mail
        return False


def pre_save_email_activation(sender, instance, *args, **kwargs):
    if not instance.activated and not instance.force_expired:
        if not instance.key:
            instance.key = unique_key_generator(instance)


pre_save.connect(pre_save_email_activation, sender=EmailActivation)


def post_save_user_create_receiver(sender, instance, created, *args, **kwargs):
    if created:
        obj = EmailActivation.objects.create(
            user=instance, email=instance.email)
        obj.send_activation()


post_save.connect(post_save_user_create_receiver, sender=User)
