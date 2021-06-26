from rest_framework import status
from rest_framework.test import APITestCase


class RegistrationUserTestCase(APITestCase):

    def test_registration(self):
        data = {'username': 'test_user',
                'email': 'test@localhost.app',
                'password1': 'strongPassword',
                'password2': 'strongPassword',
                }
        response = self.client.post('/api/rest-auth/registration/', data)
        self.assertEqual(response.status_code, status.HTTP_201_CREATED)
