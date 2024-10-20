from rest_framework import permissions

class HasValidApiKey(permissions.BasePermission):
    """
    Custom permission to only allow access if a valid API key is provided.
    """

    def has_permission(self, request, view):
        return request.auth is not None  
