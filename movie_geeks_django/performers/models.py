from django.db import models
from django.utils.text import slugify


class Performer(models.Model):
    """
    Stores information on individuals involved in the entertainment industry. This is a basic class encompassing
    all types of entertainers but can be overwritten in order to differentiate between types if appropriate.
    """

    full_name = models.CharField(max_length=50, blank=False)
    birthdate = models.DateField(blank=False)
    biography = models.TextField(max_length=1200, blank=False)
    url_name = models.SlugField(unique=True, null=True, blank=True)

    def __str__(self):
        return self.full_name

    def save(self, *args, **kwargs):
        self.url_name = slugify(self.full_name)
        super().save(*args, **kwargs)
