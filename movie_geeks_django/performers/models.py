from django.db import models
from django.utils.text import slugify


class Performer(models.Model):
    full_name = models.CharField(max_length=50, blank=False)
    birthdate = models.DateField(blank=True, null=True)
    biography = models.TextField(max_length=1000, blank=True, null=True)
    url_name = models.SlugField(unique=True, null=True, blank=True)

    def __str__(self):
        return self.full_name

    def save(self, *args, **kwargs):
        self.url_name = slugify(self.full_name)
        super().save(*args, **kwargs)
