from django.urls import path
from . import views
from .views import EventsListView, EventsDetailView, EventCreateView

urlpatterns = [
    path("events", EventsListView.as_view(), name="events"),
    path("events/<int:pk>/", EventsDetailView.as_view(), name="event-detail"),
    path("events/new/", EventCreateView.as_view(), name="create-event"),
]
