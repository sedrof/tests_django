import uuid

import jwt
from django.conf import settings
from django.http import JsonResponse
from jwt import InvalidTokenError
from rest_framework import status


class IdentityMiddleware:
    """
    Middleware to authenticate users.
    In DEBUG mode, a dummy owner user is created if request header doesn't include
    Authorization credentials.
    """

    def __init__(self, get_response):
        self.get_response = get_response

    def __call__(self, request):
        if "HTTP_AUTHORIZATION" not in request.META or not request.META[
            "HTTP_AUTHORIZATION"
        ].startswith("Bearer "):
            return JsonResponse(
                data={"detail": "Missing or invalid authorization"},
                status=status.HTTP_401_UNAUTHORIZED,
                headers={"WWW-Authenticate": "Bearer"},
                safe=False,
            )

        try:
            self.authenticate_request(request)
        except (ValueError, InvalidTokenError) as e:
            return JsonResponse(
                data={"detail": f'Bearer error="{e}"'},
                status=status.HTTP_401_UNAUTHORIZED,
                headers={"WWW-Authenticate": f'Bearer error="{e}"'},
                safe=False,
            )

        return self.get_response(request)

    def authenticate_request(self, request):
        key = settings.AUTH_VERIFYING_KEY
        token = request.META["HTTP_AUTHORIZATION"].removeprefix("Bearer ")
        identity = jwt.decode(
            jwt=token,
            key=key,
            issuer="bigcommand_account",
            audience="bigcommand_users",
            algorithms=["RS256"],
        )
        request.identity = self.update_value_types(identity)

    def update_value_types(self, identity):
        identity["user_id"] = uuid.UUID(identity["user_id"])
        identity["owner_id"] = uuid.UUID(identity["owner_id"])
        identity["permissions"] = set(identity["permissions"])
        return identity
