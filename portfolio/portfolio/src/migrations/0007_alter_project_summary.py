# Generated by Django 4.1.1 on 2022-09-20 13:11

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('src', '0006_project'),
    ]

    operations = [
        migrations.AlterField(
            model_name='project',
            name='summary',
            field=models.CharField(max_length=200),
        ),
    ]