# Generated by Django 3.0.5 on 2020-04-24 11:39

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('catalog', '0009_auto_20200424_1051'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='addbook',
            name='slug',
        ),
    ]