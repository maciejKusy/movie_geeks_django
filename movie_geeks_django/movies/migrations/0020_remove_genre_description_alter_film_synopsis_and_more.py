# Generated by Django 4.0.1 on 2022-02-14 11:55

import django.db.models.deletion
from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ("users", "0001_initial"),
        ("movies", "0019_alter_filmreview_film_reviewed"),
    ]

    operations = [
        migrations.RemoveField(
            model_name="genre",
            name="description",
        ),
        migrations.AlterField(
            model_name="film",
            name="synopsis",
            field=models.TextField(max_length=1200),
        ),
        migrations.AlterField(
            model_name="filmreview",
            name="author",
            field=models.ForeignKey(
                on_delete=django.db.models.deletion.PROTECT,
                related_name="reviews",
                to="users.userprofile",
            ),
        ),
        migrations.AlterField(
            model_name="filmreview",
            name="content",
            field=models.TextField(max_length=500),
        ),
    ]