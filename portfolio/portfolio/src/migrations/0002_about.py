# Generated by Django 4.1.1 on 2022-09-18 17:53

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('src', '0001_initial'),
    ]

    operations = [
        migrations.CreateModel(
            name='About',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('full_name', models.CharField(max_length=60)),
                ('job', models.CharField(max_length=40)),
                ('summary', models.TextField()),
                ('hobbies', models.CharField(blank=True, max_length=100, null=True)),
                ('likes', models.CharField(blank=True, max_length=100, null=True)),
            ],
        ),
    ]
