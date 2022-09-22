from django.test import TestCase
from django.urls import reverse

from portfolio.src.models import About


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
