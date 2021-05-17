from django.shortcuts import render
from .models import Event


def events(request):
    return render(request, "MainApp/events.html", {"events": Event.objects.all()})


def createEvent(request):
    return render(request, "MainApp/createEvent.html", {})
