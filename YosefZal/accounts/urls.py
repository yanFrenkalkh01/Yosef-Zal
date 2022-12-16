from django.urls import path
from . import views
from .views import ChangePasswordView

urlpatterns = [
    # Authentication urls
    path('register/', views.register_page, name="register"),
    path('login/', views.login_page, name='login'),
    path('logout/', views.logout_user, name='logout'),

    # home page urls
    path('', views.home, name="home"),
    path('home/', views.home, name="home"),
    path('home/go_find', views.go_find, name="go_find"),
    path('dashboard/', views.dashboard, name="dashboard"),

    # User urls
    path('users/', views.users, name="users"),
    path('users/meetings', views.meting_list, name='meetings'),
    path('users/complaint', views.complaint_ticket, name='complaint'),
    path('users/tickets_page', views.ticket_page, name='tickets'),
    path('users/toggle', views.toggle_true_false, name='toggle'),
    path('users/Edit_Profile', views.edit_profile, name="edit_profile"),
    path('users/password-change/', ChangePasswordView.as_view(), name='password_change'),
    path('users/Doctor/', views.user_doctor, name="doctor"),
    path('users/Patient/', views.user_patient, name="patient"),
    path('users/Administrator/', views.user_admin, name="administrator"),
    path('users/profile/', views.profile, name="profile"),
    path('users/note/', views.note, name="note"),
    path('users/appointment', views.appointment, name='appointment'),
    path('users/chat/', views.user_chat_room, name='chatroom'),
    path('users/prescriptions', views.doctor_prescriptions, name='prescriptions'),
    path('users/history', views.doctor_history, name='history'),
    path('upload', views.list, name='list'),


]


