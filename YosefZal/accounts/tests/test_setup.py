from django.test import TestCase
from django.urls import reverse
from django.contrib.auth import get_user_model


class TestSetUp(TestCase):

    def setUp(self):
        self.register_url = reverse('register')
        self.login_url = reverse('login')

        self.user = get_user_model().objects.create_user(username='test', password='12test12', email='test@example.com')
        self.user.save()

        return super().setUp

    def tearDown(self):
        self.user.delete()
        return super().tearDown()
