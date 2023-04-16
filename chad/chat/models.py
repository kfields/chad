import uuid

from django.db import models

from agent.models import Agent


class Chat(models.Model):
    id = models.UUIDField(primary_key=True, default=uuid.uuid4, editable=False)
    name = models.CharField(max_length=255, unique=True, default='New Chat')
    created_at = models.DateTimeField(auto_now_add=True)
    agents = models.ManyToManyField(Agent)

    def __str__(self):
        return self.name

"""
class Message(models.Model):
    chat = models.ForeignKey(Chat, on_delete=models.CASCADE, default=1)
    role = models.CharField(max_length=32)
    content = models.TextField()
    created_date = models.DateTimeField(auto_now_add=True)
"""

class Message(models.Model):
    content = models.TextField()
    created_at = models.DateTimeField(auto_now_add=True)
    from_agent = models.ForeignKey(Agent, related_name='from_messages', on_delete=models.CASCADE)
    chat = models.ForeignKey(Chat, related_name='messages', on_delete=models.CASCADE)
