# Generated by Django 4.1.1 on 2022-09-19 12:06

from django.db import migrations, models
import portfolio.src.validators


class Migration(migrations.Migration):

    dependencies = [
        ('src', '0003_about_img'),
    ]

    operations = [
        migrations.CreateModel(
            name='Certificate',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(max_length=40)),
                ('date', models.DateField()),
                ('validity', models.URLField(blank=True, null=True)),
            ],
        ),
        migrations.AlterField(
            model_name='about',
            name='img',
            field=models.ImageField(blank=True, null=True, upload_to='imgs/profile_img', validators=[portfolio.src.validators.MaxFileSizeInMbValidator(5)]),
        ),
    ]