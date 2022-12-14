'''
from rest_framework import status
from .test_setup import TestSetUp


class TestRegister(TestSetUp):
    def test_can_register_new_user(self):
        response = self.client.post(self.register_url, self.user_data, format="text/html")
        self.assertEqual(response.status_code, status.HTTP_302_FOUND)

'''