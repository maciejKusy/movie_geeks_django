# Generated by Django 4.0.1 on 2022-02-03 10:16

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('movies', '0004_alter_film_url_name'),
    ]

    operations = [
        migrations.AlterField(
            model_name='film',
            name='url_name',
            field=models.SlugField(blank=True, max_length=51, null=True, unique=True),
        ),
    ]
