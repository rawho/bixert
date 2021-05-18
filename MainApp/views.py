from django.shortcuts import render, redirect
from .models import Event
from django.views.generic import ListView, DetailView, CreateView
from django.views.decorators.csrf import csrf_exempt


def events(request):
    return render(request, "MainApp/events.html", {"events": Event.objects.all()})


class EventsListView(ListView):
    model = Event
    template_name = "MainApp/events.html"  # <app>/<models>_<viewtype>.html
    context_object_name = "events"
    ordering = ["-date_posted"]


class EventsDetailView(DetailView):
    model = Event


@csrf_exempt
def createEvent(request):
    if request.method == "POST":
        title = request.POST.get("title")
        content = request.POST.get("content")
        author = request.user
        Event.objects.create(title=title, content=content, author=author)
        return redirect("events")
    return render(request, "MainApp/createEvent.html", {})
