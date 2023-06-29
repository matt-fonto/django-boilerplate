from django.shortcuts import render

# Views, also known as the controller, are the functions that handle requests and return responses.

# We will pass this data to the template to display it in the browser.
rooms = [
    {
        "id": 1,
        "name": "Learn Python",
        "description": "Learn Python from scratch",
    },
    {
        "id": 2,
        "name": "Learn TypeScript",
        "description": "Learn TypeScript for frontend development",
    },
    {
        "id": 3,
        "name": "Learn Laravel",
        "description": "Learn Laravel for backend development",
    },
]


def home(request):
    # context: data that we want to pass to the template
    context = {"rooms": rooms}
    #  render(request, template_name, data)
    return render(request, "base/home.html", context)


# pk: primary key
# dynamic url routing
def room(request, pk):
    # room = we set it to None because we want to check if the room exists
    room = None
    # loop through the rooms list
    for i in rooms:
        # if the id of the room matches the pk, then set room to that room
        if i["id"] == int(pk):
            room = i
    # context: data that we want to pass to the template
    context = {"room": room}
    return render(request, "base/room.html", context)
