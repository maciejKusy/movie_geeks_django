# Generated by Django 4.0.1 on 2022-01-31 14:36

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('movies', '0001_initial'),
    ]

    operations = [
        migrations.AlterField(
            model_name='film',
            name='year_of_release',
            field=models.IntegerField(),
        ),
    ]