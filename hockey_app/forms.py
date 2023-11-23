from django.forms import ModelForm
from .models import *
from django.contrib.auth.forms import UserCreationForm, AuthenticationForm

class PlayerForm(ModelForm):
    class Meta:
        model = Player
        fields =('name', 'email', 'teamLevel', 'teamName', 'phoneNum')


class RegistrationForm(UserCreationForm):
    class Meta:
        model = CustomUser
        fields = ['username', 'email', 'password1', 'password2']

class LoginForm(AuthenticationForm):
    pass