from django.core.exceptions import ObjectDoesNotExist
from django.views.generic import TemplateView, ListView, DetailView

from portfolio.src.models import Contact, About


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
