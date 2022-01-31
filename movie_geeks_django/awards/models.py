from django.db import models


class Award(models.Model):
    name = models.CharField(max_length=50, blank=False)
    date_established = models.DateField(blank=True)
    description = models.TextField(max_length=200)

    def __str__(self):
        return self.name
