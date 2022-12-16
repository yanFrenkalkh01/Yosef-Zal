from rest_framework import status
from .test_setup import TestSetUp
from django.contrib.auth import get_user


class TestViews(TestSetUp):
    def test_user_can_view_page_register(self):
        response = self.client.get(self.register_url)
        self.assertEqual(response.status_code, status.HTTP_200_OK)

    def test_login(self):
        self.client.force_login(self.user)
        self.assertTrue(get_user(self.client).is_authenticated)
        response = self.client.get(self.patient_url)
        self.assertEqual(response.status_code, status.HTTP_200_OK)

    def test_user_can_view_home_page(self):
        response = self.client.get(self.home_url)
        self.assertEqual(response.status_code, status.HTTP_200_OK)
        self.assertTemplateUsed(response, 'accounts/home.html')

    def test_only_logged_on_user_can_view_patient_page(self):
        response = self.client.get(self.patient_url)
        self.assertEqual(response.status_code, status.HTTP_302_FOUND)

    def test_only_logged_on_user_as_can_view_administrator_page(self):
        self.client.force_login(self.user3)
        response = self.client.get(self.administrator_url)
        self.assertEqual(response.status_code, status.HTTP_200_OK)
        self.assertTemplateUsed(response, 'accounts/users/Administrator.html')

    def test_only_logged_on_user_as_can_view_doctor_page(self):
        self.client.force_login(self.user2)
        response = self.client.get(self.doctor_url)
        self.assertEqual(response.status_code, status.HTTP_200_OK)
        self.assertTemplateUsed(response, 'accounts/users/Doctor.html')

    def test_complaint_view(self):
        self.client.force_login(self.user)
        response = self.client.get(self.complaint_url)
        self.assertEqual(response.status_code, status.HTTP_200_OK)
        self.assertTemplateUsed(response, 'accounts/complaint.html')

    def test_chatroom_view(self):
        self.client.force_login(self.user)
        response = self.client.get(self.chat_room_url)
        self.assertEqual(response.status_code, status.HTTP_200_OK)
        self.assertTemplateUsed(response, 'accounts/meting_list.html')

    def test_tickets_view(self):
        self.client.force_login(self.user3)
        response = self.client.get(self.tickets_url)
        self.assertEqual(response.status_code, status.HTTP_200_OK)
        self.assertTemplateUsed(response, 'accounts/tickets_page.html')

    def test_edit_profile_view(self):
        self.client.force_login(self.user)
        response = self.client.get(self.edit_profile_url)
        self.assertEqual(response.status_code, status.HTTP_200_OK)
        self.assertTemplateUsed(response, 'accounts/users/edit_profile.html')

