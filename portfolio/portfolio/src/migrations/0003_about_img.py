# Generated by Django 4.1.1 on 2022-09-18 18:26

from django.db import migrations, models
import portfolio.src.validators


class Migration(migrations.Migration):

    dependencies = [
        ('src', '0002_about'),
    ]

    operations = [
        migrations.AddField(
            model_name='about',
            name='img',
            field=models.ImageField(blank=True, null=True, upload_to='static/imgs/profile_img', validators=[portfolio.src.validators.MaxFileSizeInMbValidator(5)]),
        ),
    ]
