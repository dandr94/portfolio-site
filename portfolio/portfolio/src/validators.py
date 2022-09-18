from django.core.exceptions import ValidationError
from django.utils.deconstruct import deconstructible


@deconstructible
class MaxFileSizeInMbValidator:
    VALIDATION_ERROR_MSG = 'File size is too big. Max size is 5 MB'

    def __init__(self, max_size):
        self.max_size = max_size

    def __call__(self, value):
        file_size = value.file.size
        if file_size > self.__mb_to_b(self.max_size):
            raise ValidationError(self.VALIDATION_ERROR_MSG)

    @staticmethod
    def __mb_to_b(value):
        return value * 1024 * 1024
