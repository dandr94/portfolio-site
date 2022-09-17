from django.views.generic import TemplateView


class Home(TemplateView):
    template_name = 'index.html'


# TODO: Make it dynamic with models etc...
class Contacts(TemplateView):
    template_name = 'contacts.html'