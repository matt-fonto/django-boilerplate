from django.urls import path
from . import views

urlpatterns = [
    # path("path", views.function, name="name")
    path("", views.home, name="home"),
    # "room/<str:pk>": "room/1 or room/2 or room/3" = dynamic url routing
    path("room/<str:pk>", views.room, name="room"),
    # create room
    path("create-room", views.createRoom, name="create-room"),
    # update room
    path("update-room/<str:pk>", views.updateRoom, name="update-room"),
    # delete room
    path("delete-room/<str:pk>", views.deleteRoom, name="delete-room"),
]
