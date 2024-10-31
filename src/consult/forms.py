from django import forms
from .models import Appointment


class AppointmentForm(forms.ModelForm):
    class Meta:
        model = Appointment
        fields = ('first_name', 'last_name', 'email',
                  'appointment_type', 'appointment_date_time', 'message')

        widgets = {
            'first_name': forms.TextInput(attrs={"class": "form-control", "placeholder": "First name"}),
            'last_name': forms.TextInput(attrs={"class": "form-control", "placeholder": "Last name"}),
            'email': forms.EmailInput(attrs={"class": "form-control", "placeholder": "Enter a valid email address"}),
            'appointment_type': forms.Select(attrs={'class': 'form-control'}),
            # 'appointment_date_time': forms.TextInput(attrs={'class': 'datetimepicker'}),
            'message': forms.Textarea(attrs={"class": "form-control"}),
        }
