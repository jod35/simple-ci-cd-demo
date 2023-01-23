from django.test import TestCase
from django.urls import reverse
from http import HTTPStatus

# Create your tests here.

class HomePageTest(TestCase):
    def test_homepage(self):
        response = self.client.get(reverse('list_posts'))

        self.assertEqual(response.status_code,HTTPStatus.OK)