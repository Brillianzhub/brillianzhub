from django.shortcuts import render, get_object_or_404
from .models import PrivacyPolicy
# Create your views here.


def privacy_policy(request):
    privacy_policy = get_object_or_404(PrivacyPolicy, id=1)

    context = {
        'privacy_policy': privacy_policy
    }
    return render(request, 'policies/privacy_policy.html', context)
