from django.contrib import admin

from portfolio.src.models import Contacts, About


@admin.register(Contacts)
class ListOfContacts(admin.ModelAdmin):
    list_display = ['name', 'value']


@admin.register(About)
class AboutInformation(admin.ModelAdmin):
    list_display = ['full_name', 'job']
