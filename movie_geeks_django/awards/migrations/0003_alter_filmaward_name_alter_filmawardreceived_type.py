# Generated by Django 4.0.1 on 2022-02-01 13:31

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('awards', '0002_filmawardreceived_type'),
    ]

    operations = [
        migrations.AlterField(
            model_name='filmaward',
            name='name',
            field=models.CharField(choices=[('oscar', 'oscar'), ('golden globe', 'golden globe'), ('golden palm', 'golden palm'), ('golden raspberry', 'golden raspberry')], max_length=50, null=True),
        ),
        migrations.AlterField(
            model_name='filmawardreceived',
            name='type',
            field=models.CharField(choices=[('oscar', 'oscar'), ('golden globe', 'golden globe'), ('golden palm', 'golden palm'), ('golden raspberry', 'golden raspberry')], max_length=50, null=True),
        ),
    ]
