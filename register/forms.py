from django import forms
from django.contrib.auth import login, authenticate
from django.contrib.auth.forms import UserCreationForm
from django.contrib.auth.models import User
from .models import Profile

#create user forms to store data

class RegisterForm(UserCreationForm): #inherit our form from Djangos UserCreationFrom
    email = forms.EmailField() #adding a field to this inheritted form

    class Meta:
        model = User
        fields = [
            "username",
            "email",
            "password1",
            "password2"
        ]

class UserUpdateForm(forms.ModelForm):
    email = forms.EmailField() #adding a field to this inheritted form

    class Meta:
        model = User
        fields = [
            "username",
            "email"
        ]

class ProfileUpdateForm(forms.ModelForm):

    class Meta:
        model = Profile
        fields = ['image']