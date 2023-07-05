from django.shortcuts import render, redirect
from .models import Room
from .forms import RoomForm

# Views, also known as the controller, are the functions that handle requests and return responses.


def home(request):
    # get all the rooms from the database
    # variable: Mdodel.objects.method()
    rooms = Room.objects.all()
    # context: data that we want to pass to the template
    context = {"rooms": rooms}
    #  render(request, template_name, data)
    return render(request, "base/home.html", context)


# pk: primary key
# dynamic url routing
def room(request, pk):
    # get the room with the given id
    room = Room.objects.get(id=pk)
    # context: data that we want to pass to the template
    context = {"room": room}
    return render(request, "base/room.html", context)


def createRoom(request):
    form = RoomForm()  # create an instance of the RoomForm

    # logic for creating a room
    if request.method == "POST":  # if the request method is POST
        form = RoomForm(
            request.POST
        )  # create an instance of the RoomForm with the data from the POST request
        if form.is_valid():  # the type of the data is correct
            form.save()  # save the data to the database
            return redirect("home")  # redirect the user to the home page

    context = {"form": form}  # pass the form to the template
    return render(request, "base/room_form.html", context)


def updateRoom(request, pk):
    room = Room.objects.get(id=pk)  # get the room with the given id
    # the form will be pre-filled with the data from the room
    form = RoomForm(instance=room)  # create an instance of the RoomForm with the room

    # logic for updating the room
    if request.method == "POST":  # if the request method is POST
        form = RoomForm(request.POST, instance=room)
        if form.is_valid():  # the type of the data is correct
            form.save()  # save the data to the database
            return redirect("home")  # redirect the user to the home page

    context = {"form": form}
    return render(request, "base/room_form.html", context)


def deleteRoom(request, pk):
    room = Room.objects.get(id=pk)  # get the room with the given id

    # logic for deleting the room
    if request.method == "POST":  # if the request method is POST
        room.delete()  # delete the room
        return redirect("home")  # redirect the user to the home page

    context = {"item": room}
    return render(request, "base/delete.html", context)
