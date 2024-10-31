import os
from django.db import models
from django.urls import reverse
import random
from django.db.models import Q
from django.db.models.signals import pre_save
from brillianzhub.utils import unique_slug_generator
from taggit.managers import TaggableManager
from django.conf import settings
from ckeditor_uploader.fields import RichTextUploadingField



class BlogQuerySet(models.query.QuerySet):

    def featured(self):
        return self.get_queryset().filter(featured=True)

    def published(self):
        return self.filter(status='published')

    def search(self, query):
        lookups = (
            Q(title__icontains=query) |
            Q(body__icontains=query) |
            Q(tags__name__in=[query])
        )
        return self.filter(lookups).distinct()


class BlogManager(models.Manager):
    def get_queryset(self):
        return BlogQuerySet(self.model, using=self._db)

    def featured(self):
        return self.get_queryset().filter(featured=True)

    def published(self):
        return self.get_queryset().published()

    def search(self, query=None):
        if query is None:
            return self.get_queryset().none()
        return self.get_queryset().published().search(query)


def get_filename_ext(filepath):
    base_name = os.path.basename(filepath)
    name, ext = os.path.splitext(base_name)
    return name, ext


def upload_image_path(instance, filename):
    new_filename = random.randint(1, 3910233549)
    name, ext = get_filename_ext(filename)
    final_filename = '{new_filename}{ext}'.format(
        new_filename=new_filename, ext=ext)
    return "blog/{new_filename}/{final_filename}".format(
        new_filename=new_filename,
        final_filename=final_filename
    )


class Category(models.Model):
    name = models.CharField(max_length=100)

    def __str__(self):
        return self.name


class Blog(models.Model):
    STATUS_CHOICES = (
        ('draft', 'Draft'),
        ('published', 'Published'),
    )
    author = models.ForeignKey(
        settings.AUTH_USER_MODEL, related_name='authored_blogs', on_delete=models.CASCADE)
    reviewed_by = models.ForeignKey(
        settings.AUTH_USER_MODEL, related_name='reviewed_blogs', on_delete=models.SET_NULL, null=True, blank=True)
    factchecked_by = models.ForeignKey(
        settings.AUTH_USER_MODEL, related_name='factchecked_blogs', on_delete=models.SET_NULL, null=True, blank=True)

    title = models.CharField(max_length=350)
    description = models.TextField(blank=True, null=True)
    category = models.ForeignKey(
        Category, related_name='blog_category', on_delete=models.CASCADE)
    slug = models.SlugField(blank=True, unique=True)
    body = RichTextUploadingField()
    publish = models.DateTimeField(auto_now=True)
    last_updated = models.DateTimeField(auto_now=True)
    created = models.DateTimeField(auto_now_add=True)
    image = models.ImageField(
        upload_to=upload_image_path, null=True, blank=True)
    featured = models.BooleanField(default=False)
    status = models.CharField(
        max_length=10, choices=STATUS_CHOICES, default='draft')
    read_time = models.IntegerField(help_text="Reading time in minutes", blank=True, null=True)
    youtube_link = models.URLField(max_length=500, blank=True, null=True)
    download_link = models.CharField(max_length=500, blank=True, null=True)
    download_audio_link = models.CharField(max_length=500, blank=True, null=True)

    objects = BlogManager()
    tags = TaggableManager()
    search = BlogManager()

    class Meta:
        ordering = ('-publish',)

    def __str__(self):
        return self.title

    def get_absolute_url(self):
        return reverse('blog:blog-detail', args=[self.slug])


def post_pre_save_receiver(sender, instance, *args, **kwargs):
    if not instance.slug:
        instance.slug = unique_slug_generator(instance)


pre_save.connect(post_pre_save_receiver, sender=Blog)


class TableOfContents(models.Model):
    blog = models.ForeignKey(
        Blog, related_name='toc_entries', on_delete=models.CASCADE)
    title = models.CharField(max_length=255)
    order = models.PositiveIntegerField()

    class Meta:
        ordering = ['order']

    def __str__(self):
        return f'{self.order}. {self.title}'


class KeyTakeaway(models.Model):
    blog = models.ForeignKey(
        Blog, related_name='key_takeaways', on_delete=models.CASCADE)
    content = models.TextField()
    order = models.PositiveIntegerField()

    class Meta:
        ordering = ['order']

    def __str__(self):
        return f'{self.order}. {self.content[:50]}...'
