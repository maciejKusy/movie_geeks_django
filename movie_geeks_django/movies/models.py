from django.core.validators import MaxValueValidator, MinValueValidator
from django.db import models
from datetime import datetime
from django.utils.text import slugify


class Film(models.Model):
    name = models.CharField(max_length=50, blank=False)
    year_of_release = models.IntegerField(default=1, validators=[
            MaxValueValidator(datetime.now().year + 2),
            MinValueValidator(1888)
        ]
    )
    synopsis = models.TextField(max_length=200, blank=False)
    director = models.ForeignKey('performers.Performer',
                                 related_name='directed',
                                 on_delete=models.PROTECT,
                                 blank=True, null=True)
    cast = models.ManyToManyField('performers.Performer', related_name='starred_in', blank=True)
    url_name = models.SlugField(unique=True, max_length=51, null=True, blank=True)

    def __str__(self):
        return f'{self.name} ({self.year_of_release})'

    def save(self, *args, **kwargs):
        self.full_clean()
        if not self.url_name:
            self.url_name = slugify(f'{self.name} {self.year_of_release}')
        super().save(*args, **kwargs)
