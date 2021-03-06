from datetime import datetime
from statistics import mean

from django.core.validators import MaxValueValidator, MinValueValidator
from django.db import models
from django.utils import timezone
from django.utils.text import slugify


class Film(models.Model):
    """
    Used for storing info on particular films released between 1888 and two years into the future on any
    given year.
    """

    name = models.CharField(max_length=50, blank=False)
    year_of_release = models.IntegerField(
        default=1,
        validators=[
            MaxValueValidator(datetime.now().year + 2),
            MinValueValidator(1888),
        ],
        blank=False,
    )
    genre = models.ManyToManyField("movies.Genre", related_name="films", blank=True)
    synopsis = models.TextField(max_length=1200, blank=False)
    director = models.ManyToManyField(
        "performers.Performer", related_name="directed", blank=True
    )
    cast = models.ManyToManyField(
        "performers.Performer", related_name="starred_in", blank=True
    )
    url_name = models.SlugField(unique=True, max_length=51, null=True, blank=True)

    def __str__(self):
        return f"{self.name} ({self.year_of_release})"

    def save(self, *args, **kwargs):
        self.full_clean()
        self.url_name = slugify(f"{self.name} {self.year_of_release}")
        super().save(*args, **kwargs)

    def get_score(self):
        """
        Used to ascertain the aggregated score of a film based on user reviews. Queries the database for
        reviews dedicated to a particular film and calculates the average score.
        """
        reviews = FilmReview.objects.all().filter(film_reviewed=self.id)
        if reviews:
            score_list = list()
            reviews_list = reviews.iterator()
            for review in reviews_list:
                score_list.append(review.rating)
            return round(mean(score_list), 1)
        return 0


class Genre(models.Model):
    """
    Used to store information on particular genres.
    """

    name = models.CharField(max_length=30, blank=False)
    url_name = models.SlugField(unique=True, max_length=40, null=True, blank=True)

    def __str__(self):
        return self.name

    def save(self, *args, **kwargs):
        self.url_name = slugify(self.name)
        super().save(*args, **kwargs)


class FilmReview(models.Model):
    """
    Stores information for individual movie reviews created by users.
    """

    author = models.ForeignKey(
        "users.UserProfile",
        related_name="reviews",
        on_delete=models.PROTECT,
        blank=True,
        null=True,
    )
    rating = models.IntegerField(
        default=1, validators=[MaxValueValidator(10), MinValueValidator(1)], blank=False
    )
    title = models.CharField(max_length=50, blank=False)
    written_on = models.DateTimeField(default=timezone.now)
    content = models.TextField(max_length=500, blank=False)
    film_reviewed = models.ForeignKey(
        Film, related_name="reviews", on_delete=models.CASCADE, blank=False, null=True
    )
    url_name = models.SlugField(unique=True, max_length=120, null=True, blank=True)

    def __str__(self):
        return f"{self.title}, {str(self.film_reviewed)} review by {str(self.author)}"

    def save(self, *args, **kwargs):
        self.url_name = slugify(f"{self.title} {str(self.author)}")
        super().save(*args, **kwargs)
