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
