from django.contrib.auth.forms import UserCreationForm, AuthenticationForm
from django.contrib.auth.views import LoginView, LogoutView
from .forms import *
from django.http import HttpResponse
from django.urls import reverse_lazy
from django.views.generic import CreateView, View

#   Логин
class RegisterView(CreateView):
    form_class = SignupForm
    template_name = 'core/register.html'
    success_url = reverse_lazy('login')


class LoginUser(LoginView):
    form_class = SigninForm
    template_name = 'core/auth.html'


class LogoutUser(LogoutView):
    next_page = '/'







