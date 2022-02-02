from django.db import models


class Performer(models.Model):
    full_name = models.CharField(max_length=50, blank=False)
    birthdate = models.DateField(blank=True, null=True)
    biography = models.TextField(max_length=400, blank=True, null=True)
    url_name = models.CharField(max_length=51, null=True, blank=True)

    def __str__(self):
        return self.full_name

    def save(self, *args, **kwargs):
        self.url_name = self.full_name.replace(' ', '_').lower()
        super(Performer, self).save(*args, **kwargs)


