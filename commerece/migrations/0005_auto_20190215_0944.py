# Generated by Django 2.1.5 on 2019-02-15 04:44

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('commerece', '0004_profile_mobile_number'),
    ]

    operations = [
        migrations.AlterField(
            model_name='profile',
            name='image',
            field=models.ImageField(upload_to='commerece/static/commerece/profile_picture'),
        ),
    ]
