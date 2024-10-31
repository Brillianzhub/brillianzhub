from django.urls import path
from . import views

app_name = 'consult'

urlpatterns = [
    path('', views.appointment_view, name='book_appointment'),
]
