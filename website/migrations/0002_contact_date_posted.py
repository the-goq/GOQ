# Generated by Django 2.1.4 on 2019-03-18 11:27

from django.db import migrations, models
import django.utils.timezone


class Migration(migrations.Migration):

    dependencies = [
        ('website', '0001_initial'),
    ]

    operations = [
        migrations.AddField(
            model_name='contact',
            name='date_posted',
            field=models.DateTimeField(default=django.utils.timezone.now),
        ),
    ]