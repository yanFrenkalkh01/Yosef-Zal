from django.test import TestCase
from django.urls import reverse
from django.contrib.auth import get_user_model
from django.contrib.auth.models import User, Group


# tset main class all the ather test classes derive from it
class TestSetUp(TestCase):
    # set up block for costume users and pages urls
    def setUp(self):
        # pages urls for unit tests
        self.register_url = reverse('register')
        self.login_url = reverse('login')
        self.home_url = reverse('home')
        self.patient_url = reverse('patient')
        self.doctor_url = reverse('doctor')
        self.administrator_url = reverse('administrator')
        self.complaint_url = reverse('complaint')
        self.chat_room_url = reverse('meetings')
        self.tickets_url = reverse('tickets')
        self.edit_profile_url = reverse('edit_profile')

        # first custom users set as patient
        self.password = '12test12'
        self.email = 'test@example.com'
        self.user = User.objects.create_user(
            username='test',
            password=self.password,
            email=self.email,
        )
        group = Group.objects.get(name='Patient')
        self.user.groups.add(group)
        self.user.save()

        # second custom users set as Doctor
        self.user2 = User.objects.create_user(
            username='test2',
            password=self.password,
            email=self.email,
        )
        group2 = Group.objects.get(name='Doctor')
        self.user2.groups.add(group2)
        self.user2.save()

        # third custom users set as Administrator
        self.user3 = User.objects.create_user(
            username='test3',
            password=self.password,
            email=self.email,
        )
        group3 = Group.objects.get(name='Administrator')
        self.user3.groups.add(group3)
        self.user3.save()

        return super().setUp

    # destruction of the costume users from the database
    def tearDown(self):
        self.user.delete()
        self.user2.delete()
        self.user3.delete()
        return super().tearDown()
