from loguru import logger
from django.conf import settings
from django.db import models
from model_utils.managers import InheritanceManager

from django.utils.translation import gettext_lazy as _

from accounts.models import User


class Agent(models.Model):
    name = models.CharField(max_length=250, default="New Agent")
    created_date = models.DateTimeField(auto_now_add=True)

    objects = InheritanceManager()
    class Meta:
        verbose_name = _("agent")
        verbose_name_plural = _("agents")

    def __str__(self):
        return self.name

class Avatar(Agent):
    user = models.OneToOneField(User, related_name='avatar', on_delete=models.CASCADE)
    class Meta:
        verbose_name = _("avatar")
        verbose_name_plural = _("avatars")

class Bot(Agent):
    class Meta:
        verbose_name = _("bot")
        verbose_name_plural = _("bots")

from django.db.models.signals import post_save
from django.dispatch import receiver

@receiver(post_save, sender=User)
def create_avatar(sender, instance, created, **kwargs):
    logger.debug('create_avatar')
    if created:
        logger.debug('Avatar created')
        Avatar.objects.create(user=instance, name=instance.username)

@receiver(post_save, sender=User)
def save_profile(sender, instance, **kwargs):
    instance.avatar.save()