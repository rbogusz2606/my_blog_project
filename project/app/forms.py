from django import forms
from .models import UserHobby
from django.contrib.auth.forms import UserCreationForm, AuthenticationForm
from django.contrib.auth.models import User

class userForm(forms.ModelForm):
    class Meta:
        model = UserHobby
        fields = "__all__"
        labels = {
            "hobby" : "Tell something about your hobby",
            "image": "Photo",
        } 


class RegisterForm(UserCreationForm):
    class Meta:
        model = User
        fields = ['username', 'email', 'password1', 'password2']


class LoginForm(AuthenticationForm):
   remember_me = forms.BooleanField(
       required=False,
       initial=True,
       widget=forms.CheckboxInput(attrs={'class': 'form-check-input'})
   )