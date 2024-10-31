from django.urls import path
from . import views

urlpatterns = [
    path('register-token/', views.register_token, name='register_token'),
    path('unregister-token/', views.delete_token, name='delete_token'),
    path('send-notification/', views.send_notification, name='send_notification'),
    path('send-test/', views.send_test_notification),
]
