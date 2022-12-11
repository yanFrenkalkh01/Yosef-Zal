from django.test import TestCase
from django.urls import reverse


class TestSetUp(TestCase):

    def setUp(self):
        self.register_url = reverse('register')
        self.login_url = reverse('login')

        self.user_data = {
            'username': 'user',
            'email': 'emai@gmail.com',
            'password1': 'pass@123',
            'password2': 'pass@123',
        }

        return super().setUp

    def tearDown(self):
        return super().tearDown()