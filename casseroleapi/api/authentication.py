from rest_framework import authentication, exceptions
from django.conf import settings

class ApiKeyAuthentication(authentication.BaseAuthentication):
    keyword = 'Bearer'

    def authenticate(self, request):
        auth_header = authentication.get_authorization_header(request).split()

        if not auth_header or auth_header[0].decode().lower() != self.keyword.lower():
            return None  # No authentication attempted

        if len(auth_header) == 1:
            msg = 'Invalid API key header. No credentials provided.'
            raise exceptions.AuthenticationFailed(msg)
        elif len(auth_header) > 2:
            msg = 'Invalid API key header. Credentials string should not contain spaces.'
            raise exceptions.AuthenticationFailed(msg)

        try:
            api_key = auth_header[1].decode()
        except UnicodeError:
            msg = 'Invalid API key header. Unable to decode credentials.'
            raise exceptions.AuthenticationFailed(msg)

        if api_key != settings.API_KEY:
            raise exceptions.AuthenticationFailed('Invalid API key.')

        return (None, api_key)
