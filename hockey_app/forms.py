from django.forms import ModelForm
from .models import *

class PlayerForm(ModelForm):
    class Meta:
        model = Player
        fields =('name', 'email', 'teamLevel', 'teamName', 'phoneNum')