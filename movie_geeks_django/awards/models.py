from django.db import models, OperationalError


class FilmAward(models.Model):
    name = models.CharField(max_length=50, blank=False)
    date_established = models.DateField(blank=True)
    description = models.TextField(max_length=200, blank=True)

    def __str__(self):
        return self.name


class FilmAwardReceived(models.Model):
    TYPES = list()
    try:
        for name in FilmAward.objects.values_list('name', flat=True).distinct():
            TYPES.append(name)
    except OperationalError:
        pass

    type = models.CharField(choices=TYPES, max_length=50, null=True)
    awarded_on = models.DateField(blank=False)
    awarded_for = models.ForeignKey('movies.Film', on_delete=models.PROTECT, blank=False)
    recipient = models.ForeignKey('performers.Performer', on_delete=models.CASCADE, blank=False)

    def __str__(self):
        return f'{self.name} received by {self.recipient} for {self.awarded_for}.'
