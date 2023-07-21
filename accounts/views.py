from django.contrib.auth.models import User
from django.shortcuts import render
from django.views.generic import DetailView

# Create your views here.



class ProfileView(DetailView):
    model = User
    template_name = 'accounts/profile.html'
    context_object_name = 'profile'
