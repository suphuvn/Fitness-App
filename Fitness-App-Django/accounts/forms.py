from django import forms
from django.contrib.auth.forms import UserCreationForm
from accounts.models import Account

class RegistrationForm(UserCreationForm):
    email = forms.EmailField(max_length=60, help_text='Required. Add a valid email address')
    first_name = forms.CharField(max_length=60, help_text='Required. Add a first name')
    last_name = forms.CharField(max_length=60, help_text='Required. Add a last name')

    class Meta:
        model = Account
        fields = ('email', 'first_name', 'last_name', 'password')
