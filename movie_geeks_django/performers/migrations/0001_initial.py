# Generated by Django 4.0.1 on 2022-01-31 14:19

from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Performer',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('full_name', models.CharField(max_length=50)),
                ('birthdate', models.DateField(blank=True)),
                ('biography', models.TextField(blank=True, max_length=400)),
            ],
        ),
    ]
