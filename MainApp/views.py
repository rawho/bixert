from django.shortcuts import render


def home(request):
    return render(request, "MainApp/home.html")

def events(request):
    return render(request, "MainApp/events.html", {
        
    })