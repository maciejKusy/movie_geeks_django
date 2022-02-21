from django.contrib.auth.models import User
from django.db import models
from django.utils import timezone


class UserProfile(models.Model):
    """
    Used to store additional user info not connected with authorisation.
    """

    user = models.OneToOneField(User, on_delete=models.CASCADE)
    date_joined = models.DateField(default=timezone.now)

    def __str__(self):
        return self.user.username
