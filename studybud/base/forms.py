from django.forms import ModelForm
from .models import Room


# Forms are used to create and update data in the database.
class RoomForm(ModelForm):
    # here we define the model that we want to create a form for
    class Meta:
        model = Room  # we want to create a form for the Room model
        fields = "__all__"  # this means that we want to include all the fields present in the Room model
