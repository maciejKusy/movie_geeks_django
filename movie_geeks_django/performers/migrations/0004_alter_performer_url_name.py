# Generated by Django 4.0.1 on 2022-02-02 14:47

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ("performers", "0003_performer_url_name"),
    ]

    operations = [
        migrations.AlterField(
            model_name="performer",
            name="url_name",
            field=models.CharField(blank=True, max_length=51, null=True),
        ),
    ]
