# Generated by Django 4.0.1 on 2022-02-13 13:39

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ("awards", "0007_filmawardreceived_award_status"),
    ]

    operations = [
        migrations.AddField(
            model_name="filmawardreceived",
            name="category",
            field=models.CharField(max_length=50, null=True),
        ),
    ]