from django.shortcuts import render
from .models import Event


def home(request):
<<<<<<< HEAD
    context = {"events": Event.objects.all()}
    return render(request, "MainApp/home.html", context)
=======
    return render(request, "MainApp/home.html")

def events(request):
    return render(request, "MainApp/events.html", {
        
    })
>>>>>>> 10b5af1f6eb793b519e479ba182c2873c2c449f8
