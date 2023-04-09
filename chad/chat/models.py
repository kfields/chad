from datetime import datetime

from django.db import models

from accounts.models import User


class Chat(models.Model):
    user = models.ForeignKey(User, on_delete=models.CASCADE, default=1)
    title = models.CharField(max_length=250, default="New Chat")
    created_date = models.DateTimeField(default=datetime.now())
    updated_date = models.DateTimeField(blank=True, null=True)

    def __str__(self):
        return self.title


class Message(models.Model):
    chat = models.ForeignKey(Chat, on_delete=models.CASCADE, default=1)
    role = models.CharField(max_length=32)
    content = models.TextField()
    created_date = models.DateTimeField(default=datetime.now())
    updated_date = models.DateTimeField(blank=True, null=True)
