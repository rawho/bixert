from django.urls import path
from . import views
from .views import EventsListView, EventsDetailView

urlpatterns = [
    path("events/", EventsListView.as_view(), name="events"),
    path("events/<int:pk>/", EventsDetailView.as_view(), name="event-detail"),
    path("events/new/", views.createEvent, name="create-event"),
    path("myevents", views.myevents, name="myevents"),
    path("registered/", views.registered, name="registered"),
    path("verify/<ids>", views.verify, name="verify"),
    path("notifications", views.notification, name="notifications"),
]
