# Generated by Django 4.1.1 on 2022-09-21 15:23

import cloudinary.models
from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('src', '0008_alter_about_img_alter_project_cover'),
    ]

    operations = [
        migrations.AlterField(
            model_name='about',
            name='img',
            field=cloudinary.models.CloudinaryField(blank=True, max_length=255, null=True),
        ),
    ]