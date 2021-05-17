from django.shortcuts import render
from .models import Event


def home(request):
    return render(request, "MainApp/home.html")


def events(request):
    return render(request, "MainApp/events.html", {
        "events" : Event.objects.all()
    })

def createEvent(request):
    return render(request, "MainApp/createEvent.html", {
        
    })