from django.contrib import admin

# Register your models here.

from .models import Room, Topic, Message

# Register the Room model with the admin site so that it can be managed via the admin interface
admin.site.register(Room)  # this is the Room model defined in studybud\base\models.py
admin.site.register(Topic)  # this is the Topic model defined in studybud\base\models.py
admin.site.register(
    Message
)  # this is the Message model defined in studybud\base\models.py
