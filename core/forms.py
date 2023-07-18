from django import forms
from django.contrib.auth.forms import UserCreationForm, AuthenticationForm



#     Формы core
from django.contrib.auth.models import User


class SignupForm(UserCreationForm):
    username = forms.CharField(label='Login', widget=forms.TextInput(attrs={'class': 'reg-input', 'placeholder': 'Username'}))
    email = forms.CharField(label='Email', widget=forms.EmailInput(attrs={'class': 'reg-input', 'placeholder': 'Email'}))
    password1 = forms.CharField(label="Password", widget=forms.PasswordInput(attrs={'class': 'reg-input', 'placeholder': 'Password'}))
    password2 = forms.CharField(label="Reset Password", widget=forms.PasswordInput(attrs={'class': 'reg-input', 'placeholder': 'Reset password'}))


    class Meta:
        model = User
        fields = ('username', 'email', 'password1', 'password2')


class SigninForm(AuthenticationForm):
    username = forms.CharField(label='Login', widget=forms.TextInput(attrs={'placeholder': 'Username'}))
    password = forms.CharField(label="Password", widget=forms.PasswordInput(attrs={'placeholder': 'Password'}))


    class Meta:
        model = User
        fields = ('username', 'password')

