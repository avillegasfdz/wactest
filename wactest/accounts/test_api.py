from django.test import TestCase
from mock import patch, MagicMock

from accounts.api import UserAccountModelViewSet
from accounts.serializers import ReadUserAccountSerializer, EditUserAccountSerializer


class UserAccountModelViewSetTestCase(TestCase):

    def test_get_serializer_class_retrieve(self):
        """Tests get_serializer_class for the retrieve action"""
        # Arrange
        api = UserAccountModelViewSet()
        api.action = 'retrieve'

        # Act
        serializer = api.get_serializer_class()

        # Assert
        self.assertEqual(serializer, ReadUserAccountSerializer)

    def test_get_serializer_class_update(self):
        """Tests get_serializer_class for the update action"""
        # Arrange
        api = UserAccountModelViewSet()
        api.action = 'update'

        # Act
        serializer = api.get_serializer_class()

        # Assert
        self.assertEqual(serializer, EditUserAccountSerializer)

    def test_get_serializer_class_partial_update(self):
        """Tests get_serializer_class for the update action"""
        # Arrange
        api = UserAccountModelViewSet()
        api.action = 'partial_update'

        # Act
        serializer = api.get_serializer_class()

        # Assert
        self.assertEqual(serializer, EditUserAccountSerializer)

    def test_get_serializer_class_other(self):
        """Tests get_serializer_class for the another action"""
        # Arrange
        api = UserAccountModelViewSet()
        api.action = 'delete'

        # Act
        serializer = api.get_serializer_class()

        # Assert
        self.assertIsNone(serializer)

    @patch('accounts.api.get_object_or_404')
    @patch('accounts.api.UserAccountModelViewSet.check_object_permissions')
    def test_get_object_with_permissions(self, mock_check_object_permissions, mock_get_object_or_404):
        """Tests get_object"""
        # Arrange
        api = UserAccountModelViewSet()
        api.kwargs = {'id': 'some_id'}  # kwargs and request are needed in get_object
        api.request = MagicMock()

        # Act
        obj = api.get_object()

        # Assert
        self.assertEqual(obj, mock_get_object_or_404.return_value)  # Return the correct object
        mock_check_object_permissions.assert_called_once_with(api.request, obj)
