from django.test import TestCase
from rest_framework import status
from rest_framework.test import APIClient


class EmailAPITest(TestCase):
    def test_send_email(self):
        client = APIClient()

        data = {
            'to_email': 'amirhosseinkhalili901@gmail.com',
            'subject': 'TEST',
            'message': 'This is a test email !'
        }

        response = client.post('/send_email/', data=data, format='json')

        self.assertEqual(response.status_code, status.HTTP_200_OK)
