from django.views.generic import TemplateView, ListView

from portfolio.src.models import Contacts


class Home(TemplateView):
    template_name = 'index.html'


class ShowContacts(ListView):
    model = Contacts
    template_name = 'contacts.html'
    context_object_name = 'contacts'

    def get_queryset(self):
        queryset = Contacts.objects.all()
        return queryset
