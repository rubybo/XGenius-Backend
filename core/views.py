from django.contrib.auth.forms import UserCreationForm, AuthenticationForm
from django.contrib.auth.views import LoginView
from django.contrib.auth.models import User
from django.urls import reverse_lazy
from django.views.generic import CreateView

#   Логин
class RegisterView(CreateView):
    model = User
    form_class = UserCreationForm
    template_name = 'core/register.html'
    success_url = reverse_lazy('login')


class LoginUser(LoginView):
    form_class = AuthenticationForm
    template_name = 'core/login.html'



