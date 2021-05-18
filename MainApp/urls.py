from django.urls import path
from . import views
from .views import EventsListView, EventsDetailView

urlpatterns = [
    path("events", EventsListView.as_view(), name="events"),
    path("events/<int:pk>/", EventsDetailView.as_view(), name="event-detail"),
    path("create-event", views.createEvent, name="create-event"),
]
