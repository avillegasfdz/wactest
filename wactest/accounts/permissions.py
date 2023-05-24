from rest_framework import permissions


class IsCurrentUser(permissions.BasePermission):
    """
    Object-level permission to only allow the current user to access its object
    """

    def has_object_permission(self, request, view, obj):
        """Overrides has_object_permission"""
        return obj == request.user
