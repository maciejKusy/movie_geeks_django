from django.contrib.auth.models import User
from django.db.models.signals import post_save
from django.dispatch import receiver

from .models import UserProfile


@receiver(post_save, sender=User)
def create_profile(sender, instance, created, **kwargs):
    """
    Ensures that whenever a user object is created, an accompanying UserProfile instance is created referencing it.
    """
    if created:
        UserProfile.objects.create(user=instance)


@receiver(post_save, sender=User)
def save_profile(sender, instance, **kwargs):
    """
    Ensures that whenever a user object instance is updated, the UserProfile instance is updated as well.
    """
    instance.userprofile.save()
