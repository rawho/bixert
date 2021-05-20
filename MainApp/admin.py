from django.contrib import admin
from .models import Event, EventUser,Chat

admin.site.register(Event)
admin.site.register(EventUser)
admin.site.register(Chat)