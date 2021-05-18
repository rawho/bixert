from django.shortcuts import render
from .models import Event
from django.views.generic import ListView,DetailView


def events(request):
    return render(request, "MainApp/events.html", {"events": Event.objects.all()})


class EventsListView(ListView):
    model = Event
    template_name = "MainApp/events.html"  # <app>/<models>_<viewtype>.html
    context_object_name = "events"
    ordering = ["-date_posted"]

class EventsDetailView(DetailView):
    model = Event
    


def createEvent(request):
    return render(request, "MainApp/createEvent.html", {})
