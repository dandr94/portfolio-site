from django.core.exceptions import ObjectDoesNotExist


def return_obj(model):
    try:
        return model.objects.get()
    except ObjectDoesNotExist:
        return False
