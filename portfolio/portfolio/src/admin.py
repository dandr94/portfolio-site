from django.contrib import admin

from portfolio.src.models import Contact, About, Certificate, Project


@admin.register(Contact)
class ListOfContacts(admin.ModelAdmin):
    list_display = ['name', 'value']


@admin.register(About)
class AboutInformation(admin.ModelAdmin):
    list_display = ['full_name', 'job']


@admin.register(Certificate)
class CertificateInformation(admin.ModelAdmin):
    list_display = ['name', 'date']


@admin.register(Project)
class ProjectInformation(admin.ModelAdmin):
    list_display = ['name', 'github_link']
