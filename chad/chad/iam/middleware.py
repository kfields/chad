from loguru import logger
import jwt

from django.contrib.auth import get_user_model
from django.http import JsonResponse
from django.conf import settings
from asgiref.sync import iscoroutinefunction, markcoroutinefunction

from django.utils.functional import SimpleLazyObject
from channels.db import database_sync_to_async

@database_sync_to_async
def get_request_user(request):
    if isinstance(request.user, SimpleLazyObject):
        request.user._setup()
    return request.user

@database_sync_to_async
def get_request_avatar(request):
    if isinstance(request.user, SimpleLazyObject):
        request.user._setup()
    return request.user.avatar

class AuthenticationMiddleware:
    async_capable = True
    sync_capable = False

    def __init__(self, get_response):
        self.get_response = get_response
        if iscoroutinefunction(self.get_response):
            markcoroutinefunction(self)

    async def __call__(self, request):
        auth_header = request.META.get("HTTP_AUTHORIZATION")
        logger.debug(auth_header)
        if auth_header and auth_header != 'Bearer undefined':
            #if not auth_header:
            #    return JsonResponse({"error": "Authentication credentials not provided"}, status=401)

            # Check if the header starts with 'Bearer '
            if not auth_header.startswith('Bearer '):
                return JsonResponse({"error": "Invalid token format"}, status=401)

            # Extract the token from the header
            token = auth_header[7:]
            
            user_model = get_user_model()
            try:
                #user = user_model.objects.get(auth_token=token)
                payload = jwt.decode(token, settings.SECRET_KEY, algorithms="HS256")
                #user = user_model.objects.get(id=payload["id"])
                user = await user_model.objects.aget(id=payload["id"])
                logger.debug(user)

            except user_model.DoesNotExist:
                return JsonResponse({"error": "Invalid token"}, status=401)

            request.user = user

        response = await self.get_response(request)
        return response
