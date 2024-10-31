from django.db import models


class Appointment(models.Model):
    NUMBER_CHOICES = (
        ('1', 'Stock Investment'),
        ('2', 'Real Estate'),
        ('4', 'Personal Finance'),
        ('more than 3', 'Others'),
    )
    first_name = models.CharField(max_length=20)
    last_name = models.CharField(max_length=20)
    email = models.EmailField()
    appointment_type = models.CharField(
        max_length=15, choices=NUMBER_CHOICES, default='1')
    appointment_date_time = models.DateTimeField()
    message = models.CharField(max_length=100)
    created = models.DateTimeField(auto_now_add=True)

    class Meta:
        ordering = ('created',)

    def __str__(self):
        return self.first_name
