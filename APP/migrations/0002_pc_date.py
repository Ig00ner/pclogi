# Generated by Django 5.1.6 on 2025-02-12 08:53

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('APP', '0001_initial'),
    ]

    operations = [
        migrations.AddField(
            model_name='pc',
            name='date',
            field=models.DateTimeField(auto_now=True),
        ),
    ]
