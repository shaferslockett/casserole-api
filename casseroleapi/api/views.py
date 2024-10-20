
from .models import Casserole
from .serializers import CasseroleSerializer
from rest_framework.views import APIView
from rest_framework.response import Response
from rest_framework import status
from rest_framework.permissions import AllowAny, IsAuthenticated
from django.shortcuts import get_object_or_404
from django.conf import settings
from .permissions import HasValidApiKey

# Views

class CasseroleList(APIView):
    permission_classes = [HasValidApiKey]
    def get(self, request):
        casseroles = Casserole.objects.all()
        names = [casserole.name for casserole in casseroles]
        return Response(names, status=status.HTTP_200_OK)

class CasseroleDetail(APIView):
    permission_classes = [HasValidApiKey]
    def get(self, request, name):
        try:
            casserole = Casserole.objects.get(name=name)
            serializer = CasseroleSerializer(casserole)
            return Response(serializer.data, status=status.HTTP_200_OK)
        except Casserole.DoesNotExist:
            return Response(
                {'error': 'Casserole not found.'},
                status=status.HTTP_404_NOT_FOUND
            )

class ObtainApiKeyView(APIView):
    permission_classes = [AllowAny]  # Allow unrestricted access to this view

    def post(self, request):
        # Extract username and password from the request data
        username = request.data.get('username')
        password = request.data.get('password')

        # Hardcoded credentials
        HARD_CODED_USERNAME = "guest"
        HARD_CODED_PASSWORD = "12345"

        # Validate the credentials
        if username == HARD_CODED_USERNAME and password == HARD_CODED_PASSWORD:
            # Credentials are valid; return the API key
            api_key = settings.API_KEY
            return Response(
                {'api_key': api_key},
                status=status.HTTP_200_OK
            )
        else:
            # Credentials are invalid; return an error response
            return Response(
                {'error': 'Invalid username or password.'},
                status=status.HTTP_401_UNAUTHORIZED
            )