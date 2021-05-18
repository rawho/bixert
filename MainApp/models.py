from django.db import models
from django.utils import timezone
from django.contrib.auth.models import User


class Event(models.Model):
    title = models.CharField(max_length=100)
    content = models.TextField()
    banner = models.ImageField(default="banner/quiz.png", upload_to="banner")
    # date_posted = models.DateTimeField(auto_now_add=True)
    date_posted = models.DateTimeField(default=timezone.now)
    author = models.ForeignKey(User, on_delete=models.CASCADE)

    def __str__(self):
        return self.title
