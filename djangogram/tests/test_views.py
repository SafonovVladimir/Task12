from django.test import TestCase, Client
from django.urls import reverse
from djangogram.models import *
import json


class TestView(TestCase):

    def test_project_GET(self):
        client = Client()
        response = client.get(reverse('home'))

        self.assertEqual(response.status_code, 200)
        self.assertTemplateUsed(response, 'djangogram/index.html')



