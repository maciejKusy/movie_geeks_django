# Generated by Django 4.0.1 on 2022-02-13 14:56

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ("awards", "0011_remove_filmawardreceived_name_filmawardreceived_type"),
    ]

    operations = [
        migrations.RenameField(
            model_name="filmawardreceived",
            old_name="type",
            new_name="name",
        ),
    ]
