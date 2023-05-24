from django.test import TestCase
from mock import MagicMock

from accounts.permissions import IsCurrentUser


class IsCurrentUserTestCase(TestCase):

    def test_has_object_permission_equal(self):
        """Tests the has_object_permission method for when the object and user are the same"""
        # Arrange
        permission = IsCurrentUser()
        mock_obj = MagicMock()
        mock_view = MagicMock()
        mock_request = MagicMock()
        mock_request.user = mock_obj  # request.user is the same as the object

        # Act
        has_permission = permission.has_object_permission(
            mock_request,
            mock_view,
            mock_obj
        )

        # Assert
        self.assertTrue(has_permission)

    def test_has_object_permission_equal(self):
        """Tests the has_object_permission method for when the object and user are different"""
        # Arrange
        permission = IsCurrentUser()
        mock_obj = MagicMock()
        mock_view = MagicMock()
        mock_request = MagicMock()  # request.user should be an object different from mock_obj

        # Act
        has_permission = permission.has_object_permission(
            mock_request,
            mock_view,
            mock_obj
        )

        # Assert
        self.assertFalse(has_permission)
