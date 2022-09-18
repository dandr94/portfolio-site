from django.contrib import admin

from portfolio.src.models import Contacts


@admin.register(Contacts)
class ListOfContacts(admin.ModelAdmin):
    list_display = ['name', 'value']
