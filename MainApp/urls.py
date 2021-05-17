from django.urls import path
from . import views

urlpatterns = [
    path("", views.home, name="MainApp-home"),
    path("events", views.events, name='events'),
    path("create-event", views.createEvent, name='create-event'),
]
