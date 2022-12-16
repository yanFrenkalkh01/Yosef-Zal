from django.contrib import admin
from .models import Profile, UserEvent, UserComplaints
# Register your models here.

admin.site.register(Profile)
admin.site.register(UserEvent)
admin.site.register(UserComplaints)

