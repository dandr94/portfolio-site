import datetime

from django.test import TestCase
from django.urls import reverse

from portfolio.src.models import About, Contact, Certificate
from portfolio.src.views import ShowContacts, CertificateDetails


class AboutMeViewTests(TestCase):
    VALID_ABOUT_ME_CREDENTIALS = {
        'full_name': 'Test Testov',
        'job': 'Testing stuff',
        'summary': 'I am testing stuff'
    }

    def test_expect_correct_template(self):
        response = self.client.get(reverse('about'))
        self.assertTemplateUsed('about_me.html')

    def test_context_with_valid_credentials(self):
        about = About.objects.create(**self.VALID_ABOUT_ME_CREDENTIALS)
        about.save()

        response = self.client.get(reverse('about'))
        about_context = response.context['about']

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

    def test_expect_correct_template(self):
        response = self.client.get(reverse('contacts'))
        self.assertTemplateUsed('contacts.html')

    def test_context_with_credentials(self):
        contacts = Contact.objects.create(**self.VALID_CONTACT_CREDENTIALS)
        contacts.save()
        response = self.client.get(reverse('contacts'))
        view = ShowContacts()
        view.response = response

        qs = view.get_queryset()

        self.assertQuerysetEqual(qs, Contact.objects.all())


class CertificateDetailsViewTests(TestCase):
    VALID_CERTIFICATE_CREDENTIALS = {
        'name': 'Python Basics',
        'date': datetime.date(2020, 5, 13),
    }

    def test_expect_correct_template(self):
        response = self.client.get(reverse('certificates'))
        self.assertTemplateUsed('certificates.html')

    def test_context_with_credentials(self):
        certificates = Certificate.objects.create(**self.VALID_CERTIFICATE_CREDENTIALS)
        certificates.save()
        response = self.client.get(reverse('certificates'))
        view = CertificateDetails()
        view.response = response

        qs = view.get_queryset()

        self.assertQuerysetEqual(qs, Certificate.objects.all())
