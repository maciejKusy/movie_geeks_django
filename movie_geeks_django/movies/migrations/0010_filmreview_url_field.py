# Generated by Django 4.0.1 on 2022-02-08 15:37

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('movies', '0009_filmreview'),
    ]

    operations = [
        migrations.AddField(
            model_name='filmreview',
            name='url_field',
            field=models.SlugField(blank=True, max_length=120, null=True, unique=True),
        ),
    ]
