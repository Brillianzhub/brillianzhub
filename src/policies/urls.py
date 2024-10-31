from django.urls import path
from . import views


app_name = 'policies'

urlpatterns = [
    path('', views.privacy_policy, name="privacy_policy")
]
