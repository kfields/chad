from loguru import logger
from django.contrib.auth.models import User
from django.db.models.signals import post_save
from django.dispatch import receiver
from .models import Avatar

#TODO: Not working for some reason.  Had to put signals in models.py

@receiver(post_save, sender=User)
def create_avatar(sender, instance, created, **kwargs):
    logger.debug('create_avatar')
    if created:
        logger.debug('Avatar created')
        Avatar.objects.create(user=instance, name=instance.username)

@receiver(post_save, sender=User)
def save_profile(sender, instance, **kwargs):
    instance.avatar.save()