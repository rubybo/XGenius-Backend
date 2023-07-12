from django.contrib.auth.forms import UserCreationForm
from django.contrib.auth.models import User
from django.urls import reverse_lazy
from django.views.generic import CreateView


class RegisterView(CreateView):
    model = User
    form_class = UserCreationForm
    template_name = ...
    success_url = reverse_lazy('login')
