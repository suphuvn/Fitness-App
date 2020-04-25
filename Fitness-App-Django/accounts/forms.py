from django import forms
from django.contrib.auth.forms import UserCreationForm
from django.contrib.auth.models import User

class RegistrationForm(UserCreationForm):
    email = forms.EmailField(max_length=60)
    first_name = forms.CharField(max_length=60)
    last_name = forms.CharField(max_length=60)

    class Meta:
        model = User
        fields = ('email', 'first_name', 'last_name', 'username', 'password1', 'password2')
