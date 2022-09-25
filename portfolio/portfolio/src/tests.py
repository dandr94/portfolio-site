import datetime

from django.test import TestCase
from django.urls import reverse

from portfolio.src.models import About, Contact, Certificate, Project
from portfolio.src.views import ShowContacts, CertificateDetails, ShowProjects


def get_context_with_credentials(self, credentials, model, template):
    model_name = model.objects.create(**credentials)
    model_name.save()

    response = self.client.get(reverse(template))
    model_name_context = response.context[template]

    return model_name_context


def get_queryset_context_with_credentials(self, credentials, model, template, view):
    model_name = model.objects.create(**credentials)
    model_name.save()
    response = self.client.get(reverse(template))
    view_name = view()
    view_name.response = response

    qs = view_name.get_queryset()

    return qs


class AboutMeViewTests(TestCase):
    VALID_ABOUT_ME_CREDENTIALS = {
        'full_name': 'Test Testov',
        'job': 'Testing stuff',
        'summary': 'I am testing stuff'
    }

    MODEL = About
    TEMPLATE = 'about'

    def test_expect_correct_template(self):
        response = self.client.get(reverse('about'))
        self.assertTemplateUsed('about_me.html')

    def test_context_with_valid_credentials(self):
        about_context = get_context_with_credentials(self, self.VALID_ABOUT_ME_CREDENTIALS, self.MODEL, self.TEMPLATE)

        self.assertEqual('Test Testov', about_context.full_name)
        self.assertEqual('Testing stuff', about_context.job)
        self.assertEqual('I am testing stuff', about_context.summary)
        self.assertEqual(None, about_context.img)
        self.assertEqual(None, about_context.hobbies)
        self.assertEqual(None, about_context.likes)

    def test_context_with_invalid_credentials__should_return_false(self):
        response = self.client.get(reverse('about'))
        about_context = response.context['about']

        self.assertEqual(False, about_context)


class HomeViewTests(TestCase):

    def test_expect_correct_template(self):
        response = self.client.get(reverse('index'))
        self.assertTemplateUsed('index.html')


class ShowContactsViewTests(TestCase):
    VALID_CONTACT_CREDENTIALS = {
        'name': 'Discord',
        'value': 'testtestov#0904'
    }

    MODEL = Contact
    TEMPLATE = 'contacts'
    VIEW = ShowContacts

    def test_expect_correct_template(self):
        response = self.client.get(reverse('contacts'))
        self.assertTemplateUsed('contacts.html')

    def test_context_with_credentials(self):
        qs = get_queryset_context_with_credentials(self, self.VALID_CONTACT_CREDENTIALS, self.MODEL, self.TEMPLATE,
                                                   self.VIEW)

        self.assertQuerysetEqual(qs, Contact.objects.all())


class CertificateDetailsViewTests(TestCase):
    VALID_CERTIFICATE_CREDENTIALS = {
        'name': 'Python Basics',
        'date': datetime.date(2020, 5, 13),
    }

    MODEL = Certificate
    TEMPLATE = 'certificates'
    VIEW = CertificateDetails

    def test_expect_correct_template(self):
        response = self.client.get(reverse('certificates'))
        self.assertTemplateUsed('certificates.html')

    def test_context_with_credentials(self):
        qs = get_queryset_context_with_credentials(self, self.VALID_CERTIFICATE_CREDENTIALS, self.MODEL, self.TEMPLATE,
                                                   self.VIEW)

        self.assertQuerysetEqual(qs, Certificate.objects.all())


class ShowProjectsViewTests(TestCase):
    VALID_SHOWPROJECTS_CREDENTIALS = {
        'name': 'TestingProject',
        'summary': 'Testing small stuff',
        'cover': 'https://res.cloudinary.com/dpdcgsg6l/image/upload/v1663857725/default-cover-bg_x7gl5j.png'
    }

    MODEL = Project
    TEMPLATE = 'projects'
    VIEW = ShowProjects

    def test_expect_correct_template(self):
        response = self.client.get(reverse('projects'))
        self.assertTemplateUsed('projects.html')

    def test_context_with_credentials(self):
        qs = get_queryset_context_with_credentials(self, self.VALID_SHOWPROJECTS_CREDENTIALS, self.MODEL, self.TEMPLATE,
                                                   self.VIEW)

        self.assertQuerysetEqual(qs, Project.objects.all())
