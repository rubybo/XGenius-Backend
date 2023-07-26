from django.contrib import admin


# Register your models here.
from .models import Message, Comment

admin.site.register(Message)
admin.site.register(Comment)
