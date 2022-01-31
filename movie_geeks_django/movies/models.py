from django.db import models
from datetime import datetime


class Film(models.Model):

    YEAR_CHOICES = list()
    for year in range(1888, datetime.now().year + 1):
        YEAR_CHOICES.append((year, year))

    name = models.CharField(max_length=50, blank=False)
    year_of_release = models.DateField(choices=YEAR_CHOICES)
    synopsis = models.TextField(max_length=200, blank=False)
    director = models.ForeignKey('performers.Performer', on_delete=models.PROTECT, blank=True, null=True)
    cast = models.ManyToManyField('performers.Performer', related_name='films', blank=True)

    def __str__(self):
        return f'{self.name} ({self.year_of_release})'
