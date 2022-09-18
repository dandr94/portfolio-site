from django.db import models


class Contacts(models.Model):
    NAME_MAX_LEN = 40
    ICON_MAX_LEN = 60
    VALUE_MAX_LEN = 40

    name = models.CharField(
        max_length=NAME_MAX_LEN,
        null=False,
        blank=False, )

    icon_class_name = models.CharField(
        max_length=ICON_MAX_LEN,
    )

    value = models.CharField(
        max_length=VALUE_MAX_LEN,
        null=False,
        blank=False,
    )

    def __str__(self):
        return f'{self.name}: {self.value}'


class About(models.Model):
    FIRST_NAME_MAX_LEN = 60
    JOB_MAX_LEN = 40
    HOBBIES_MAX_LEN = 100
    LIKES_MAX_LEN = 100

    full_name = models.CharField(
        max_length=FIRST_NAME_MAX_LEN,
        null=False,
        blank=False
    )

    job = models.CharField(
        max_length=JOB_MAX_LEN,
        null=False,
        blank=False
    )

    summary = models.TextField(
        null=False,
        blank=False
    )

    hobbies = models.CharField(
        max_length=
        HOBBIES_MAX_LEN,
        blank=True,
        null=True)

    likes = models.CharField(
        max_length=LIKES_MAX_LEN,
        blank=True,
        null=True)
