from django.views.generic import CreateView, FormView, ListView, View
from django.contrib.auth import authenticate, login, get_user_model
from django.http import HttpResponse, HttpResponseRedirect
from django.shortcuts import render, redirect, get_object_or_404
from django.urls import reverse_lazy, reverse
from django.contrib.auth.mixins import LoginRequiredMixin
from django.contrib import messages
from django.contrib.auth.decorators import login_required
from django.utils.decorators import method_decorator
from .forms import UserLoginForm, RegistrationForm, UserEditForm, ProfileEditForm, ContactForm, ReactivateEmailForm
from .models import Profile, Contact, EmailActivation
from django.views.generic.edit import FormMixin
from django.core.mail import send_mail
from django.utils.safestring import mark_safe
from .signals import user_logged_in
from django.utils.http import is_safe_url
from brillianzhub.mixins import NextUrlMixin, RequestFormAttachMixin


@login_required
def account_home_view(request):
    return render(request, "accounts/home.html", {})


class AccountHomeView(LoginRequiredMixin, ListView):
    # model = Course
    template_name = 'users/home.html'

    def get_object(self):
        return self.request.user

    def get_queryset(self):
        qs = super(AccountHomeView, self).get_queryset()
        return qs.filter(students__in=[self.request.user])

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)


class AccountEmailActivationView(FormMixin, View):
    success_url = reverse_lazy('accounts:login')
    form_class = ReactivateEmailForm
    key = None

    def get(self, request, key=None, *args, **kwargs):
        self.key = key
        if key is not None:
            qs = EmailActivation.objects.filter(key__iexact=key)
            confirm_qs = qs.confirmable()
            if confirm_qs.count() == 1:
                obj = confirm_qs.first()
                obj.activate()
                messages.success(
                    request, "Your email has been confirmed. Please login.")
                return redirect("accounts:login")
            else:
                activated_qs = qs.filter(activated=True)
                if activated_qs.exists():
                    reset_link = reverse("password_reset")
                    msg = """Your email has already been confirmed.
                    Do you need to <a href="{link}"> reset your password</a>?""".format(link=reset_link)
                    messages.success(request, mark_safe(msg))
                    return redirect("accounts:login")
        context = {'form': self.get_form(), 'key': key}
        return render(request, 'registration/activation_error.html', context)

    def post(self, request, *args, **kwargs):
        form = self.get_form()
        if form.is_valid():
            return self.form_valid(form)
        else:
            return self.form_invalid(form)

    def form_valid(self, form):
        msg = """Activation link sent, please check your email and activate your account."""
        request = self.request
        messages.success(request, msg)
        email = form.cleaned_data.get("email")
        obj = EmailActivation.objects.email_exists(email).first()
        user = obj.user
        new_activation = EmailActivation.objects.create(user=user, email=email)
        new_activation.send_activation()

        return super(AccountEmailActivationView, self).form_valid(form)

    def form_invalid(self, form):
        context = {'form': form, 'key': self.key}
        return render(self.request, 'registration/activation_error.html', context)


class LoginView(NextUrlMixin,  RequestFormAttachMixin, FormView):
    form_class = UserLoginForm
    success_url = '/'
    template_name = 'users/login.html'
    default_next = '/'

    def form_valid(self, form):
        next_path = self.get_next_url()
        return redirect(next_path)


User = get_user_model()


def register_page(request):
    if request.method == 'POST':
        user_form = RegistrationForm(request.POST)

        if user_form.is_valid():
            # Create a new user object but avoid saving it yet
            new_user = user_form.save(commit=False)
            # Set the chosen password
            new_user.set_password(user_form.cleaned_data['password'])
            # Save the User object
            new_user.save()

            return render(request,
                          'users/register_done.html',
                          {'new_user': new_user})
    else:
        user_form = RegistrationForm()
    return render(request, 'users/register.html', {'user_form': user_form})


User = get_user_model()


def register_referrer_view(request, ref_code=None, *args, **kwargs):
    user = User.objects.get(id_referrer__iexact=ref_code)

    if request.method == 'POST':
        user_form = RegistrationForm(request.POST)

        if user_form.is_valid():
            new_user = user_form.save(commit=False)

            new_user.set_password(user_form.cleaned_data['password'])

            new_user.save()

            return render(request, 'users/register_done.html', {'new_user': new_user})

        else:
            user_form = RegistrationForm()
        return render(request, 'users/register.html', {'user_form', user_form})

# @login_required


def edit(request):
    if request.method == 'POST':
        user_form = UserEditForm(instance=request.user, data=request.POST)
        profile_form = ProfileEditForm(instance=request.user.profile,
                                       data=request.POST,
                                       files=request.FILES)
        if user_form.is_valid() and profile_form.is_valid():
            user_form.save()
            profile_form.save()
            return HttpResponseRedirect(reverse_lazy('home'))
        else:
            messages.error(request, 'Error updating your profile')
    else:
        user_form = UserEditForm(instance=request.user)
        profile_form = ProfileEditForm(instance=request.user.profile)
    return render(request,
                  'users/edit.html',
                  {'user_form': user_form,
                   'profile_form': profile_form})


def contact(request):
    sent = False

    if request.method == 'POST':
        contact_form = ContactForm(request.POST)

        if contact_form.is_valid():
            name = contact_form.cleaned_data['name']
            message = contact_form.cleaned_data['message']
            sender = contact_form.cleaned_data['sender']
            cc_myself = contact_form.cleaned_data['cc_myself']

            recipients = ['brillianzhub@gmail.com']
            if cc_myself:
                recipients.append(sender)

                send_mail(name, message, sender, recipients)
                contact_form.save()
                sent = True
            else:
                send_mail(name, message, sender, recipients)
                contact_form.save()
                sent = True
    else:
        contact_form = ContactForm()

    context = {
        "contact_form": contact_form,
        "sent": sent,
    }
    template = 'users/contactus.html'
    return render(request, template, context)


def message_sent(request):
    return (request, 'users/message_sent.html')
