# Generated by Django 3.0.5 on 2020-04-26 16:18

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('catalog', '0012_auto_20200426_1616'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='addbook',
            name='slug',
        ),
    ]
