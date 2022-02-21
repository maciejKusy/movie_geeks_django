# Generated by Django 4.0.1 on 2022-02-14 11:55

import django.db.models.deletion
from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ("movies", "0019_alter_filmreview_film_reviewed"),
        ("performers", "0007_alter_performer_biography_alter_performer_birthdate"),
        ("awards", "0013_alter_filmaward_name_and_more"),
    ]

    operations = [
        migrations.AlterField(
            model_name="filmaward",
            name="date_established",
            field=models.DateField(),
        ),
        migrations.AlterField(
            model_name="filmaward",
            name="description",
            field=models.TextField(max_length=200),
        ),
        migrations.AlterField(
            model_name="filmaward",
            name="name",
            field=models.CharField(max_length=50),
        ),
        migrations.AlterField(
            model_name="filmawardreceived",
            name="award_status",
            field=models.CharField(
                choices=[("winner", "winner"), ("nominee", "nominee")], max_length=20
            ),
        ),
        migrations.AlterField(
            model_name="filmawardreceived",
            name="awarded_for",
            field=models.ForeignKey(
                on_delete=django.db.models.deletion.PROTECT, to="movies.film"
            ),
        ),
        migrations.AlterField(
            model_name="filmawardreceived",
            name="category",
            field=models.CharField(max_length=50),
        ),
        migrations.AlterField(
            model_name="filmawardreceived",
            name="name",
            field=models.ForeignKey(
                on_delete=django.db.models.deletion.CASCADE, to="awards.filmaward"
            ),
        ),
        migrations.AlterField(
            model_name="filmawardreceived",
            name="recipient",
            field=models.ForeignKey(
                on_delete=django.db.models.deletion.CASCADE,
                related_name="awards",
                to="performers.performer",
            ),
        ),
    ]