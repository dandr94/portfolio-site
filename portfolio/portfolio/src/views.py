from django.core.exceptions import ObjectDoesNotExist
from django.views.generic import TemplateView, ListView, DetailView

from portfolio.src.models import Contact, About, Certificate, Project


class Home(TemplateView):
    template_name = 'index.html'


class ShowContacts(ListView):
    model = Contact
    template_name = 'contacts.html'
    context_object_name = 'contacts'

    def get_queryset(self):
        queryset = Contact.objects.all()
        return queryset


class AboutDetails(TemplateView):
    model = About
    template_name = 'about_me.html'

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        try:
            context['about'] = About.objects.get()
        except ObjectDoesNotExist:
            context['about'] = False

        return context


class CertificateDetails(ListView):
    model = Certificate
    template_name = 'certificates.html'
    context_object_name = 'certificates'

    def get_queryset(self):
        queryset = Certificate.objects.all()
        return queryset


class ShowProjects(ListView):
    model = Project
    template_name = 'projects.html'
    context_object_name = 'projects'

    def get_queryset(self):
        queryset = Project.objects.all()
        return queryset


    def get_context_data(self, *, object_list=None, **kwargs):
        context = super().get_context_data(**kwargs)
        context['counter'] = 0
        return context
