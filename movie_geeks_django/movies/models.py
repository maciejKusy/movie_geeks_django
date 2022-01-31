from django.contrib.auth import forms
from django.db import models
from datetime import datetime


class Film(models.Model):
    name = models.CharField(max_length=50, blank=False)
    year_of_release = models.IntegerField(blank=False)
    synopsis = models.TextField(max_length=200, blank=False)
    director = models.ForeignKey('performers.Performer', on_delete=models.PROTECT, blank=True, null=True)
    cast = models.ManyToManyField('performers.Performer', related_name='films', blank=True)

    def __str__(self):
        return f'{self.name} ({self.year_of_release})'

    def clean(self):
        if self.year_of_release < 1888 or self.year_of_release > datetime.now().year:
            raise forms.ValidationError('Invalid year provided!')


