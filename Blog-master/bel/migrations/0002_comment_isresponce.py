# Generated by Django 3.0.2 on 2020-01-07 12:50

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('bel', '0001_initial'),
    ]

    operations = [
        migrations.AddField(
            model_name='comment',
            name='isResponce',
            field=models.BooleanField(default=False),
        ),
    ]