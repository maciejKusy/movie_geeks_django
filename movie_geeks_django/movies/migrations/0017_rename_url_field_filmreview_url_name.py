# Generated by Django 4.0.1 on 2022-02-13 16:11

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('movies', '0016_alter_film_genre'),
    ]

    operations = [
        migrations.RenameField(
            model_name='filmreview',
            old_name='url_field',
            new_name='url_name',
        ),
    ]
