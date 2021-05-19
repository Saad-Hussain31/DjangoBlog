#create a form that inherits from UserCreation form
from django import forms
from django.contrib.auth.models import User
from django.contrib.auth.forms import UserCreationForm

class UserRegisterForm(UserCreationForm):
    email = forms.EmailField()

    class Meta: #gives nested namespace for config and keep configs same
        model = User
        fields = ['username', 'email', 'password1', 'password2']