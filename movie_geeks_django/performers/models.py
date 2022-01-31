from django.db import models


class Performer(models.Model):
    full_name = models.CharField(max_length=50, blank=False)
    birthdate = models.DateField(blank=True)
    biography = models.TextField(max_length=400, blank=True)

    def __str__(self):
        return self.full_name
