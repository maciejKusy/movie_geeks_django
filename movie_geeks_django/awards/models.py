from django.db import models
from django.utils.text import slugify

from performers.models import Performer


class FilmAwardReceived(models.Model):
    AWARD_STATUSES = [
        ('winner', 'winner'),
        ('nominee', 'nominee'),
    ]
    name = models.ForeignKey(
        "awards.FilmAward", on_delete=models.CASCADE, blank=True, null=True
    )
    awarded_on = models.DateField(blank=False)
    award_status = models.CharField(max_length=20, choices=AWARD_STATUSES, blank=False, default='winner')
    category = models.CharField(max_length=50, blank=False, default='category')
    awarded_for = models.ForeignKey(
        "movies.Film", on_delete=models.PROTECT, blank=True, null=True
    )
    recipient = models.ForeignKey(
        "performers.Performer",
        related_name="awards",
        on_delete=models.CASCADE,
        blank=True,
        null=True
    )
    url_name = models.SlugField(unique=True, null=True, blank=True)

    def __str__(self):
        return f"{str(self.name)} received by {str(self.recipient)} for {str(self.awarded_for)}."

    def save(self, *args, **kwargs):
        self.url_name = slugify(
            f"{str(self.name)} {self.awarded_on} {str(self.recipient)}"
        )
        super().save(*args, **kwargs)


class FilmAward(models.Model):
    name = models.CharField(max_length=50, blank=False, default='award')
    date_established = models.DateField(blank=True)
    description = models.TextField(max_length=200, blank=True)
    url_name = models.SlugField(unique=True, null=True, blank=True)

    def __str__(self):
        return self.name

    def save(self, *args, **kwargs):
        if not self.url_name:
            self.url_name = slugify(self.name)
        super().save(*args, **kwargs)

    @property
    def get_all_recipients(self):
        all_awards_of_same_type = (
            FilmAwardReceived.objects.all().filter(name=self.id).values()
        )
        recipients = list()
        for award in all_awards_of_same_type.iterator():
            recipient_id = award["recipient_id"]
            recipient_name = (
                Performer.objects.all()
                .filter(pk=recipient_id)
                .values("full_name")[0]["full_name"]
            )
            recipients.append({"id": recipient_id, "full_name": recipient_name})

        return recipients
