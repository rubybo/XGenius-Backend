from django.contrib.auth.mixins import LoginRequiredMixin
from django.shortcuts import render
from django.views.generic import ListView

from .models import Message
# Create your views here



class ForumList(LoginRequiredMixin, ListView):
    model = Message
    template_name = 'forum/listforum.html'
    paginate_by = 4
