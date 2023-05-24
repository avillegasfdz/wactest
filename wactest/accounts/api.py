from rest_framework.generics import get_object_or_404
from rest_framework.permissions import IsAuthenticated
from rest_framework.viewsets import ModelViewSet

from accounts.models import UserAccount
from accounts.permissions import IsCurrentUser
from accounts.serializers import EditUserAccountSerializer, ReadUserAccountSerializer


class UserAccountModelViewSet(ModelViewSet):
    lookup_field = 'id'
    action_serializers = {
        'retrieve': ReadUserAccountSerializer,
        'update': EditUserAccountSerializer,
        'partial_update': EditUserAccountSerializer,
    }

    permissions_serializers = {
        'retrieve': [IsAuthenticated(), IsCurrentUser()],
        'update': [IsAuthenticated(), IsCurrentUser()],
        'partial_update': [IsAuthenticated(), IsCurrentUser()],
    }

    def get_serializer_class(self):
        """Override get_serializer_class to return the action serializer"""
        if hasattr(self, 'action'):
            if self.action in self.action_serializers:
                return self.action_serializers[self.action]

    def get_permissions(self):
        """Override get_permissions to return the permission serializer"""
        if hasattr(self, 'action'):
            if self.action in self.permissions_serializers:
                return self.permissions_serializers[self.action]

    def get_queryset(self):
        """Override get_queryset with all UserAccount objects"""
        return UserAccount.objects.all()

    def get_object(self):
        """Override get_object to check object permissions"""
        obj = get_object_or_404(self.get_queryset(), pk=self.kwargs["id"])
        self.check_object_permissions(self.request, obj)
        return obj
