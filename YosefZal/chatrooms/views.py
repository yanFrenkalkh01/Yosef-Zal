from django.shortcuts import render, redirect
from django.views import View
from .models import ChatRoom, Chat
from django.contrib.auth.mixins import LoginRequiredMixin
from django.contrib.auth.models import User
# Create your views here.


class Index(LoginRequiredMixin, View):
    login_url = '/login'

    def get(self, request):
        return render(request, 'chatrooms/index.html')


class Room(LoginRequiredMixin, View):
    login_url = '/login'

    def get(self, request, room_name):
        room = ChatRoom.objects.filter(name=room_name).first()
        chats = []

        if room:
            chats = Chat.objects.filter(room=room)
        else:
            room = ChatRoom(name=room_name)
            room.save()

        context = {'room_name': room_name, 'chats': chats}
        return render(request, 'chatrooms/room.html', context)
