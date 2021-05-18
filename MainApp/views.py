from django.shortcuts import render, redirect
from .models import Event, EventUser
from django.views.generic import ListView, DetailView, CreateView, View
from django.views.decorators.csrf import csrf_exempt
from django.core.files.storage import FileSystemStorage
from django.contrib.auth.models import User
from django.contrib.auth.decorators import login_required


def myevents(request):
    return render(
        request,
        "MainApp/events.html",
        {
            "events": Event.objects.filter(author=request.user.id),
            "Users": EventUser.objects.all(),
        },
    )


class EventsListView(ListView, View):
    model = Event
    template_name = "MainApp/events.html"  # <app>/<models>_<viewtype>.html
    context_object_name = "events"
    ordering = ["date_posted"]

    def get(self, request, *args, **kwargs):
        if "register" in request.GET:
            event = request.GET.get("event")
            event = Event.objects.all().filter(id=1).first()
            EventUser.objects.create(
                registered_event=event, registered_user=request.user
            )
        return render(
            request,
            template_name=self.template_name,
            context={"events": Event.objects.all(), "request": request},
        )


class EventsDetailView(DetailView):
    model = Event


@csrf_exempt
def createEvent(request):
    if request.method == "POST" and request.FILES["banner"]:
        title = request.POST.get("title")
        content = request.POST.get("content")
        author = request.user
        date = request.POST.get("date")
        max_participants = request.POST.get("maxParticipants")
        location = request.POST.get("location")
        if location == "venue":
            location = request.POST.get("place")
        banner = request.FILES["banner"]
        fs = FileSystemStorage()
        filename = fs.save(banner.name, banner)
        Event.objects.create(
            title=title,
            content=content,
            author=author,
            banner=filename,
            venue=location,
            date_posted=date,
            max_participants=max_participants,
        )
        return redirect("events")
    return render(request, "MainApp/createEvent.html", {})
