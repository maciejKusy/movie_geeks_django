# Generated by Django 4.0.1 on 2022-02-13 16:15

import django.db.models.deletion
from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ("movies", "0017_rename_url_field_filmreview_url_name"),
    ]

    operations = [
        migrations.AlterField(
            model_name="filmreview",
            name="film_reviewed",
            field=models.ForeignKey(
                null=True,
                on_delete=django.db.models.deletion.CASCADE,
                related_name="reviews",
                to="movies.film",
            ),
        ),
    ]