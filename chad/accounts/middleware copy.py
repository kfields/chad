from loguru import logger
import jwt

from django.contrib.auth import get_user_model
from django.http import JsonResponse
from django.conf import settings
#from chad.iam.jwt import decode_auth_token

"""
class AuthenticationMiddleware:
    def __init__(self, get_response):
        self.get_response = get_response

    def __call__(self, request):
        token = request.META.get("HTTP_AUTHORIZATION")
        logger.debug(token)
        if not token:
            return JsonResponse({"error": "Authentication credentials not provided"}, status=401)

        user_model = get_user_model()
        try:
            #user = user_model.objects.get(auth_token=token)
            #payload = decode_auth_token(request)
            payload = jwt.decode(token, settings.SECRET_KEY, algorithms="HS256")
            user = user_model.objects.get(id=payload["id"])
            logger.debug(user)
        except user_model.DoesNotExist:
            return JsonResponse({"error": "Invalid token"}, status=401)

        request.user = user
        response = self.get_response(request)
        return response
"""

class AuthenticationMiddleware:
    def __init__(self, get_response):
        self.get_response = get_response

    def __call__(self, request):
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
                user = user_model.objects.get(id=payload["id"])
                logger.debug(user)

            except user_model.DoesNotExist:
                return JsonResponse({"error": "Invalid token"}, status=401)

            request.user = user

        response = self.get_response(request)
        return response
