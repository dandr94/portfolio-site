from django.db import models

from portfolio.src.validators import MaxFileSizeInMbValidator


class Contact(models.Model):
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
    MAX_FILE_SIZE_IN_MB = 5
    IMG_FILE_UPLOAD_DIR = 'imgs/profile_img'
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

    img = models.ImageField(
        upload_to=IMG_FILE_UPLOAD_DIR,
        null=True,
        blank=True,
        validators=[
            MaxFileSizeInMbValidator(MAX_FILE_SIZE_IN_MB)
        ]
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


class Certificate(models.Model):
    NAME_MAX_LEN = 40

    name = models.CharField(
        max_length=NAME_MAX_LEN,
        blank=False,
        null=False
    )

    date = models.DateField(
        blank=False,
        null=False
    )

    validity = models.URLField(
        blank=True,
        null=True
    )


class Project(models.Model):
    NAME_MAX_LEN = 40
    SUMMARY_MAX_LEN = 200
    IMG_FILE_UPLOAD_DIR = 'imgs/project_img'
    DEFAULT_COVER_IMG_DIR = 'imgs/default-cover-bg.png'
    MAX_FILE_SIZE_IN_MB = 5

    name = models.CharField(
        max_length=NAME_MAX_LEN,
        blank=False,
        null=False
    )

    summary = models.CharField(
        max_length=SUMMARY_MAX_LEN,
        blank=False,
        null=False
    )

    site_link = models.URLField(
        blank=True,
        null=True
    )

    github_link = models.URLField(
        blank=True,
        null=True
    )

    cover = models.ImageField(
        upload_to=IMG_FILE_UPLOAD_DIR,
        default=DEFAULT_COVER_IMG_DIR,
        null=True,
        blank=True,
        validators=[
            MaxFileSizeInMbValidator(MAX_FILE_SIZE_IN_MB)
        ]
    )
