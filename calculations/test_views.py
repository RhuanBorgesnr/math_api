from rest_framework.test import APITestCase
from rest_framework import status
from django.urls import reverse
from calculations.models import CalculationHistory
from calculations.lib import Numbers
from unittest.mock import patch

class AverageViewTests(APITestCase):
  def setUp(self):
    self.url = reverse('average')  # Ensure you have the correct URL name

  @patch.object(Numbers, 'average', return_value=5.0)
  def test_average_post_success(self, mock_average):
    data = {
      "numbers": [1, 2, 3, 4, 5]
    }
    response = self.client.post(self.url, data, format='json')
    self.assertEqual(response.status_code, status.HTTP_200_OK)
    self.assertEqual(response.data, {"average": 5.0})
    self.assertTrue(CalculationHistory.objects.filter(operation="average").exists())

  def test_average_post_invalid_data(self):
    data = {
      "numbers": "invalid_data"
    }
    response = self.client.post(self.url, data, format='json')
    self.assertEqual(response.status_code, status.HTTP_400_BAD_REQUEST)