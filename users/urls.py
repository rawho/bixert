from django.urls import path
from . import views
from django.contrib.auth import views as auth_views

urlpatterns = [
    path("logout/", views.logout_view, name="logout"),
    path("messaging/", views.messaging, name="messaging"),
]
