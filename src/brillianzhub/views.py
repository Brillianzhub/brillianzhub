from django.http import HttpResponse, JsonResponse, HttpResponseRedirect
from django.shortcuts import render, redirect, get_list_or_404
from django.views.generic import ListView
from accounts.forms import ContactForm
from accounts.models import Contact
from django.core.mail import send_mail, BadHeaderError

from blog.models import Blog
from .utils import count_words

from collections import defaultdict


def index_view(request):


    posts = Blog.objects.filter(featured=True).published()


    context = {
        # 'course': course,
        'posts': posts,
        'seo_title': 'Brillianzhub',
        'og_title': 'Brillianzhub',
        'seo_description': 'Your Personal Investment Training Hub, where expert insights and time-tested strategies converge to pave the path to financial success and stability',
        'og_description': 'Your Personal Investment Training Hub, where expert insights and time-tested strategies converge to pave the path to financial success and stability',
    }
    return render(request, 'index.html', context)


def contact_view(request):
    if request.method == 'GET':
        form = ContactForm()
    else:
        form = ContactForm(request.POST)
        if form.is_valid():
            first_name = form.cleaned_data['first_name']
            last_name = form.cleaned_data['last_name']
            email_address = form.cleaned_data['email_address']
            subject = form.cleaned_data['subject']
            message = form.cleaned_data['message']
            recipients = ['brillianzhub@gmail.com']

            try:
                send_mail(subject, message, email_address,  recipients)
                form.save()
            except BadHeaderError:
                return HttpResponse('Invalid header found.')
            return redirect('home')
        else:
            form = ContactForm(request.POST)
    return render(request, 'base/contact.html', {'form': form, })


def success(request):
    return HttpResponse('Success! Thank you for your message.')


def about_view(request):
    context = {
        'seo_title': 'About Brillianzhub',
        'og_title': 'About Brillianzhub',
        'seo_title': 'Your Personal Investment Training Hub, where expert insights and time-tested strategies converge to pave the path to financial success and stability',
        'og_title': 'Your Personal Investment Training Hub, where expert insights and time-tested strategies converge to pave the path to financial success and stability',
    }
    return render(request, 'base/about.html', context)
