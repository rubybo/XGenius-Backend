from django.contrib.auth.mixins import LoginRequiredMixin
from django.contrib.auth.models import User
from django.views.generic import DetailView

# Core CBV



class ProfileView(LoginRequiredMixin, DetailView):
    model = User
    template_name = 'accounts/profile.html'
    context_object_name = 'profile'



