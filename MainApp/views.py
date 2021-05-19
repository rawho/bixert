from django.shortcuts import render, redirect
from .models import Event, EventUser
from django.views.generic import ListView, DetailView, CreateView, View
from django.views.decorators.csrf import csrf_exempt
from django.core.files.storage import FileSystemStorage
from django.contrib.auth.models import User
from django.contrib.auth.decorators import login_required
import json
import requests
from django.http import JsonResponse


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

    def post(self, request, *args, **kwargs):
        self.x = json.loads(request.body.decode())
        event = Event.objects.all().filter(title__contains=self.x["search_value"])
        d = []

        for eve in event:
            d.append(
                {
                    "title": eve.title,
                    "content": eve.content,
                    "venue": eve.venue,
                    "author": eve.author.username,
                    "id": eve.id,
                    "image": f"/media/{eve.banner}",
                    "date": eve.date_posted.strftime(" %d-%b-%Y"),
                    "if_reg": True
                    if request.user
                    in [
                        x.registered_user
                        for x in EventUser.objects.all().filter(registered_event=eve)
                    ]
                    else False,
                    "user": request.user.username,
                }
            )
        d = json.dumps(d)
        print(d)
        return JsonResponse(d, safe=False)

    def get(self, request, *args, **kwargs):

        if "register" in request.GET:
            event_id = request.GET.get("event")
            event = Event.objects.all().filter(id=event_id).first()
            event_user = (
                EventUser.objects.all()
                .filter(registered_event=event)
                .filter(registered_user=request.user)
                .first()
            )
            if not event_user:
                EventUser.objects.create(
                    registered_event=event, registered_user=request.user
                )
        return render(
            request,
            template_name=self.template_name,
            context={
                "events": Event.objects.all(),
                "request": request,
                "if_list": [
                    eve.registered_event.id
                    for eve in EventUser.objects.all().filter(
                        registered_user=request.user
                    )
                ],
            },
        )


def registered(request):
    if EventUser.objects.all().filter(registered_user=request.user):
        context = {
            "events": EventUser.objects.all().filter(registered_user=request.user)
        }
    else:
        context = {"events": None}

    return render(request, "MainApp/registered.html", context)


class EventsDetailView(DetailView):
    model = Event

    def get_context_data(self, **kwargs):
        context = super(EventsDetailView, self).get_context_data(**kwargs)
        context["attendees"] = [
            eve.registered_user
            for eve in EventUser.objects.all().filter(
                registered_event=self.kwargs["pk"]
            )
        ]
        return context


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
