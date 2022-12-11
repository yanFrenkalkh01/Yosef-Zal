from django.urls import path
from . import views

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
    path('users/Doctor/', views.user_doctor, name="doctor"),
    path('users/Patient/', views.user_patient, name="patient"),
    path('users/Administrator/', views.user_admin, name="administrator"),


]

