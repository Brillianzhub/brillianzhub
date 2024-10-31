# backends.py
from django.contrib.auth.backends import BaseBackend
from .models import IPrayUser


class EmailAuthBackend(BaseBackend):
    def authenticate(self, request, email=None, password=None):
        try:
            user = IPrayUser.objects.get(email=email)
            # Ensure the password is hashed correctly
            if user.check_password(password):
                return user
        except IPrayUser.DoesNotExist:
            return None

    def get_user(self, user_id):
        try:
            return IPrayUser.objects.get(pk=user_id)
        except IPrayUser.DoesNotExist:
            return None
