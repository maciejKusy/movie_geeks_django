# Generated by Django 4.0.1 on 2022-02-14 12:11

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('users', '0001_initial'),
        ('movies', '0021_alter_filmreview_author'),
    ]

    operations = [
        migrations.AlterField(
            model_name='filmreview',
            name='author',
            field=models.ForeignKey(blank=True, null=True, on_delete=django.db.models.deletion.PROTECT, related_name='reviews', to='users.userprofile'),
        ),
    ]
