from django.urls import path
from django.views.generic import TemplateView
from .views import *


#   Урл паттерны
urlpatterns = [
    path('', TemplateView.as_view(template_name='core/index.html'), name='home'),
    path('register', RegisterView.as_view(), name='register'),
    path('login', LoginUser.as_view(), name='login'),
    path('logout', LogoutUser.as_view(), name='logout'),
    path('accounts/login/', LoginUser.as_view(), name='block'),



]
