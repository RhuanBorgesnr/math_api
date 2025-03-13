from rest_framework.test import APITestCase
from rest_framework import status
from django.urls import reverse
from calculations.models import CalculationHistory
from calculations.lib import Numbers
from unittest.mock import patch

class CalculationTests(APITestCase):
    @classmethod
    def setUpTestData(cls):
        cls.average_url = reverse('average')
        cls.sum_url = reverse('sum')

    @patch.object(Numbers, 'average', return_value=5.0)
    def test_average_success(self, mock_average):
        response = self.client.post(self.average_url, {"numbers": [1, 2, 3, 4, 5]}, format='json')
        self.assertEqual(response.status_code, status.HTTP_200_OK)
        self.assertEqual(response.data, {"average": 5.0})
        self.assertTrue(CalculationHistory.objects.filter(operation="average").exists())

    @patch.object(Numbers, 'sum', return_value=15)
    def test_sum_success(self, mock_sum):
        response = self.client.post(self.sum_url, {"numbers": [1, 2, 3, 4, 5]}, format='json')
        self.assertEqual(response.status_code, status.HTTP_200_OK)
        self.assertEqual(response.data, {"sum": 15})
        self.assertTrue(CalculationHistory.objects.filter(operation="sum").exists())

    def test_invalid_data(self):
        for url in [self.average_url, self.sum_url]:
            with self.subTest(url=url):
                response = self.client.post(url, {"numbers": "invalid"}, format='json')
                self.assertEqual(response.status_code, status.HTTP_400_BAD_REQUEST)
                response = self.client.post(url, {"numbers": []}, format='json')
                self.assertEqual(response.status_code, status.HTTP_400_BAD_REQUEST)
                response = self.client.post(url, {"numbers": [1, "a", 3]}, format='json')
                self.assertEqual(response.status_code, status.HTTP_400_BAD_REQUEST)
