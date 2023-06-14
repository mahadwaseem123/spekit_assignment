from django.contrib.auth import authenticate
from rest_framework import authentication
from rest_framework import exceptions
import base64


class BasicAuthentication(authentication.BaseAuthentication):
    def authenticate(self, request):
        auth_header = request.headers.get('Authorization')
        if not auth_header:
            return None

        auth = auth_header.split()

        if len(auth) != 2:
            raise exceptions.AuthenticationFailed('Invalid authentication header')

        if auth[0].lower() != b'basic':
            raise exceptions.AuthenticationFailed('Invalid authentication header')

        username, password = base64.b64decode(auth[1]).decode().split(':', 1)

        user = authenticate(username=username, password=password)

        if user is None:
            raise exceptions.AuthenticationFailed('Invalid username/password.')

        return (user, None)