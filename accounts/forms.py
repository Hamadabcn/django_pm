from django.contrib.auth.forms import AuthenticationForm
from django import forms

attrs = {'class': 'form-control'}


class UserLoginForm(AuthenticationForm):
    def __init__(self, *args, **kwargs):
        super(UserLoginForm, self).__init__(*args, **kwargs)

    username = forms.CharField(
        label='Username',
        widget=forms.TextInput(attrs=attrs)
    )
    password = forms.CharField(
        label='Password',
        widget=forms.PasswordInput(attrs=attrs)
    )
