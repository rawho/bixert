from django.contrib import admin
from .models import Event, EventUser

admin.site.register(Event)
admin.site.register(EventUser)