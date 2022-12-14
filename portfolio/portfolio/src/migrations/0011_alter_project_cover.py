# Generated by Django 4.1.1 on 2022-09-21 15:48

import cloudinary.models
from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('src', '0010_alter_about_img'),
    ]

    operations = [
        migrations.AlterField(
            model_name='project',
            name='cover',
            field=cloudinary.models.CloudinaryField(blank=True, default='imgs/default-cover-bg.png', max_length=255, null=True),
        ),
    ]
