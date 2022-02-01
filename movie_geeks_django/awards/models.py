from django.db import models, OperationalError
from .constants import AWARD_TYPES


class FilmAward(models.Model):
    name = models.CharField(choices=AWARD_TYPES, max_length=50, blank=False, null=True)
    date_established = models.DateField(blank=True)
    description = models.TextField(max_length=200, blank=True)

    def __str__(self):
        return self.name


class FilmAwardReceived(models.Model):
    type = models.CharField(choices=AWARD_TYPES, max_length=50, blank=False, null=True)
    awarded_on = models.DateField(blank=False)
    awarded_for = models.ForeignKey('movies.Film', on_delete=models.PROTECT, blank=False)
    recipient = models.ForeignKey('performers.Performer', related_name='awards', on_delete=models.CASCADE, blank=False)

    def __str__(self):
        return f'{self.type} received by {self.recipient} for {self.awarded_for}.'
