from django.urls import path, include
from django.views.generic import TemplateView
from .views import RegisterView

urlpatterns = [
    path('', TemplateView.as_view(template_name='core/index.html'), name='home'),
    path('register/', RegisterView.as_view(), name='register'),

]
