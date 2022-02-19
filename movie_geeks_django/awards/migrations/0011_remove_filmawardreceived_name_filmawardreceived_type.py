# Generated by Django 4.0.1 on 2022-02-13 14:53

import django.db.models.deletion
from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ("awards", "0010_alter_filmawardreceived_awarded_for"),
    ]

    operations = [
        migrations.RemoveField(
            model_name="filmawardreceived",
            name="name",
        ),
        migrations.AddField(
            model_name="filmawardreceived",
            name="type",
            field=models.ForeignKey(
                blank=True,
                null=True,
                on_delete=django.db.models.deletion.CASCADE,
                to="awards.filmaward",
            ),
        ),
    ]
