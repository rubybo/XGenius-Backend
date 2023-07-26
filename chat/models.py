from django.contrib.auth.models import User
from django.db import models

# Create your models here.
class Chat(models.Model):
    """Модель для чата """
    user = models.ForeignKey(User, on_delete=models.CASCADE)
    message = models.TextField()
    response = models.TextField()
    created_at = models.DateTimeField(auto_now_add=True)