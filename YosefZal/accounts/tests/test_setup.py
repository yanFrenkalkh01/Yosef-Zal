from django.test import TestCase
from django.urls import reverse
from django.contrib.auth import get_user_model
from django.contrib.auth.models import User


class TestSetUp(TestCase):

    def setUp(self):
        self.register_url = reverse('register')
        self.login_url = reverse('login')
        self.home_url = reverse('home')
        self.patient_url = reverse('patient')

        self.password = '12test12'
        self.email = 'test@example.com'
        self.user = User.objects.create_user(
            username='test',
            password=self.password,
            email=self.email,
        )
        self.user.save()

        return super().setUp

    def tearDown(self):
        self.user.delete()
        return super().tearDown()
