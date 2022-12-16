from rest_framework import status
from .test_setup import TestSetUp
from django.contrib.auth.models import User, Group


class TestRegister(TestSetUp):
    def test_can_register_new_user(self):
        # test post response
        response = self.client.post(
            self.register_url,
            data={
                'username': User.get_username(self.user),
                'password1': self.password,
                'password2': self.password,
                'email': self.email,
                },
            format="text/html",
        )
        self.assertEqual(response.status_code, status.HTTP_200_OK)

        # test if the user was crated
        user = User.get_username(self.user)
        self.assertEqual(user, 'test')

    def test_if_user_can_login(self):
        username = User.get_username(self.user)
        password = self.password
        login = self.client.login(username=username, password=password)
        self.assertTrue(login)


