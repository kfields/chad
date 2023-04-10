from loguru import logger

from channels.db import database_sync_to_async
from chad.schema.types.base import mutation

from ..models import User
from chad.iam.jwt import encode_auth_token

@mutation.field("signIn")
#@database_sync_to_async
def resolve_signin(_, info, input):
    logger.debug(f"Login {input}")

    email = input['email']
    password = input['password']

    if not email:
        logger.debug("Email is missing")
        raise Exception('Email missing!')
    if not password:
        logger.debug("Password is missing")
        raise Exception('Password missing!')
    try:
        user = User.objects.get(email=email)
    except User.DoesNotExist:
        user = None

    if user is None or not user.check_password(password):
        logger.debug("No such user or invalid password")
        raise Exception('No such user or invalid password!')

    # Identity can be any data that is json serializable
    # TODO: handle role properly
    access_token = encode_auth_token(sub=email, id=user.id, role='Admin')
    logger.debug(f"Access token: {access_token}")
    # token = json.dumps({"token": access_token.decode('utf-8')})
    #token = access_token.decode('utf-8')
    #logger.debug(f"Token: {token}")
    return {'token': access_token}
