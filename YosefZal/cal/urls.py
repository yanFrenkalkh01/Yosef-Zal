from django.urls import re_path, path
from . import views

app_name = 'cal'
urlpatterns = [
    path('', views.base_calendar, name='cal'),
    re_path(r'^index/$', views.index, name='index'),
    re_path(r'^calendar/$', views.CalendarView.as_view(), name='calendar'),
    path(r'^event/new/$', views.event, name='event_new'),
    re_path(r'^event/edit/(?P<event_id>\d+)/$', views.event, name='event_edit'),

]
