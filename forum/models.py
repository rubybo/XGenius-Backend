from django.contrib.auth.models import User
from django.db import models

# Create your models here.


class Message(models.Model):
    message = models.TextField()
    text = models.TextField()
    user = models.OneToOneField(User, on_delete=models.CASCADE)
    comment = models.OneToOneField('Comment', on_delete=models.CASCADE)


class Comment(models.Model):
    text = models.TextField()
    user = models.OneToOneField(User, on_delete=models.CASCADE)