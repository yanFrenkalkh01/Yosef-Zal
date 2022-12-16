# -*- coding: utf-8 -*-
from PIL import Image
from django.contrib.auth.models import User, Group
from datetime import timezone
from django.db import models
from cal.models import Event # noqa


class Document(models.Model):
    docfile = models.FileField(upload_to='documents/%Y/%m/%d')


class Profile(models.Model):
    user = models.OneToOneField(User, on_delete=models.CASCADE)
    avatar = models.ImageField(default='happy-bearded-young-man.jpg', upload_to='profile_images')

    profile_number = models.CharField(max_length=20, default=0000)

    event = models.OneToOneField(Event, on_delete=models.CASCADE, blank=True, null=True)

    def __str__(self):
        return self.user.username

    # resizing images
    def save(self, *args, **kwargs):
        super().save()

        img = Image.open(self.avatar.path)

        if img.height > 100 or img.width > 100:
            new_img = (300, 200)
            img.thumbnail(new_img)
            img.save(self.avatar.path)


class UserEvent(models.Model):
    patient = models.ForeignKey(Profile, on_delete=models.CASCADE)
    doctor = models.CharField('Doctor Name', max_length=20)
    doctor_type = models.CharField('Doctor Type', max_length=20, blank=True, null=True)

    event_name = models.CharField('Event Name', max_length=20, blank=True, null=True)
    event_date = models.DateField('Event Date', blank=True, null=True)
    event_time = models.TimeField('Event Time', blank=True, null=True)
    description = models.TextField(blank=True)

    def __str__(self):
        return self.event_name

    def save(self, *args, **kwargs):
        super().save()


class UserComplaints(models.Model):
    complaint = models.TextField()
    profile = models.ForeignKey(Profile, on_delete=models.CASCADE)
    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)
    open_close = models.BooleanField(default=False)

    def save(self, *args, **kwargs):
        super().save()
