# Generated by Django 3.0.5 on 2020-04-23 04:29

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('catalog', '0001_initial'),
    ]

    operations = [
        migrations.AlterField(
            model_name='addbook',
            name='image',
            field=models.ImageField(upload_to='user_book/'),
        ),
    ]
