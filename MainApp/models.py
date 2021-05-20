from django.db import models
from django.utils import timezone
from django.contrib.auth.models import User
import datetime


class Event(models.Model):
    title = models.CharField(max_length=100)
    content = models.TextField()
    banner = models.ImageField(default="banner/quiz.png", upload_to="banner")
    venue = models.CharField(max_length=50)
    max_participants = models.IntegerField()
    # date_posted = models.DateTimeField(auto_now_add=True)
    date_posted = models.DateTimeField(default=timezone.now)
    time = models.TimeField(auto_now=False, auto_now_add=False, default=datetime.datetime.now())
    author = models.ForeignKey(User, on_delete=models.CASCADE)

    def __str__(self):
        return self.title


class EventUser(models.Model):
    registered_user = models.ForeignKey(User, on_delete=models.CASCADE)
    registered_event = models.ForeignKey(Event, on_delete=models.CASCADE)
    confirm = models.BooleanField(default=False)
