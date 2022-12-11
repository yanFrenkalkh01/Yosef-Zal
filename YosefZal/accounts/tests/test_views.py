from rest_framework import status
from .test_setup import TestSetUp


class TestViews(TestSetUp):
    def test_user_can_view_page_register(self):
        response = self.client.get(self.register_url)
        self.assertEqual(response.status_code, status.HTTP_200_OK)
        self.assertTemplateUsed(response, 'accounts/auth/register.html')
