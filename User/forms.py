from django import forms 
from django.contrib.auth.forms import UserCreationForm, AuthenticationForm
from .models import User
from django.core.validators import RegexValidator

class RegistrationForm(UserCreationForm):
    class Meta:
        model = User
        fields = ['fname' , 'lname' , 'email', 'phonenumber']


class LoginForm(forms.Form):
    email = forms.EmailField(error_messages={'error': 'email field is invalid'})
    password = forms.CharField(widget=forms.PasswordInput)    