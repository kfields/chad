from loguru import logger

from django.apps import AppConfig


class AgentConfig(AppConfig):
    default_auto_field = 'django.db.models.BigAutoField'
    name = 'agent'

    #TODO: Not working for some reason.  Had to put signals in models.py
    """
    def ready(self):
        logger.debug('AgentConfig.ready')
        from . import signals
    """