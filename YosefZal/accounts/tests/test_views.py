from rest_framework import status
from .test_setup import TestSetUp


class TestViews(TestSetUp):
    def test_user_can_view_page_register(self):
        response = self.client.get(self.register_url)
        self.assertEqual(response.status_code, status.HTTP_200_OK)
        self.assertTemplateUsed(response, 'accounts/auth/register.html')

    def test_user_can_view_login_page(self):
        response = self.client.get(self.login_url)
        self.assertEqual(response.status_code, status.HTTP_200_OK)
        self.assertTemplateUsed(response, 'accounts/auth/login.html')

    def test_user_can_view_home_page(self):
        response = self.client.get(self.home_url)
        self.assertEqual(response.status_code, status.HTTP_200_OK)
        self.assertTemplateUsed(response, 'accounts/home.html')

    def test_only_logged_on_user_can_view_patient_page(self):
        response = self.client.get(self.patient_url)
        self.assertEqual(response.status_code, status.HTTP_302_FOUND)


