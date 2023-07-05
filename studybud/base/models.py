from django.db import models
from django.contrib.auth.models import User

# Models, also known as the model, are the classes that define the structure of the data.

# Create your models here.


# Topic
class Topic(models.Model):
    name = models.CharField(max_length=100)

    # here we define the string representation of the model, so that we can see the name of the topic in the admin interface
    def __str__(self):
        return self.name


# Room
# models.Model is the base class for all models, it provides the essential fields and methods
class Room(models.Model):
    # host: one to many relationship, one user can have many rooms, but one room can only belong to one user
    host = models.ForeignKey(User, on_delete=models.SET_NULL, null=True)
    # topic: one to many relationship, one topic can have many rooms, but one room can only belong to one topic
    topic = models.ForeignKey(Topic, on_delete=models.SET_NULL, null=True)
    name = models.CharField(max_length=100)
    description = models.TextField(
        null=True, blank=True
    )  # null=True means that the field is optional
    # participants = models
    updated_at = models.DateTimeField(
        auto_now=True
    )  # auto_now=True means that the field is updated every time the model is saved
    created_at = models.DateTimeField(
        auto_now_add=True
    )  # auto_now_add=True means that the field is updated only when the model is created

    # Sort by newest room first
    class Meta:
        ordering = ["-updated_at", "-created_at"]

    # this is the string representation of the model
    def __str__(self):
        return self.name


class Message(models.Model):
    # user: one to many relationship, one user can have many messages, but one message can only belong to one user
    user = models.ForeignKey(User, on_delete=models.CASCADE)
    # room: one to many relationship, one room can have many messages, but one message can only belong to one room
    room = models.ForeignKey(
        Room, on_delete=models.CASCADE
    )  # when a room is deleted, all the messages in that room will be deleted as well
    body = models.TextField()
    updated_at = models.DateTimeField(
        auto_now=True
    )  # auto_now=True means that the field is updated every time the model is saved
    created_at = models.DateTimeField(
        auto_now_add=True
    )  # auto_now_add=True means that the field is updated only when the model is created

    # we use the __str__ method to define the string representation of the model, so that we can see the body of the message in the admin interface
    def __str__(self):
        return self.body[0:50]
