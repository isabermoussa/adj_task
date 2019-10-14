from django.test import TestCase, Client
from django.urls import reverse

from dataset.views import DatasetViewSet
# Create your tests here.


class TestViews(TestCase):
    
    def setUp(self):
        self.client = Client()

    def test_dataset_list_GET(self):
        response = self.client.get(reverse('dataset-list'))
        self.assertEquals(response.status_code, 200)