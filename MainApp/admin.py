from django.contrib import admin
from .models import Event, EventUser,Notifications

admin.site.register(Event)
admin.site.register(EventUser)
admin.site.register(Notifications)