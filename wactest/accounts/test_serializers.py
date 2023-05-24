from django.test import TestCase

from accounts.models import UserAccount
from accounts.serializers import ReadUserAccountSerializer, EditUserAccountSerializer


class ReadUserAccountSerializerTestCase(TestCase):

    def test_meta(self):
        """Tests the META class of the ReadUserAccountSerializer"""
        # Arrange
        serializer = ReadUserAccountSerializer()

        # Act - Nothing to act

        # Assert
        self.assertEqual(serializer.Meta.model, UserAccount)  # Model is correct
        self.assertEqual(serializer.Meta.fields,
                         ['username', 'first_name', 'last_name', 'email', 'avatar'])  # Fields are not changed
        self.assertEqual(serializer.Meta.read_only_fields,
                         ['username', 'first_name', 'last_name', 'email', 'avatar'])  # ReadOnly Fields are not changed

    # Left this test as example of SerializedMethodField test.
    # @patch('accounts.serializers.base64')
    # def test_get_avatar(self, mock_base_64):
    #     """Tests the get_avatar method of the ReadUserAccountSerializer"""
    #     # Arrange
    #     serializer = ReadUserAccountSerializer()
    #     mock_user_account = MagicMock()
    #
    #     # Act
    #     result = serializer.get_avatar(mock_user_account)
    #
    #     # Assert
    #     mock_base_64.b64encode.assert_called_once_with(
    #         mock_user_account.avatar.file.read.return_value
    #     )  # Stored file is encoded
    #     self.assertEqual(
    #         result,
    #         mock_base_64.b64encode.return_value
    #     )  # Result of the encoding is return


class EditUserAccountSerializerTestCase(TestCase):

    def test_meta(self):
        """Tests the META class of the EditUserAccountSerializer"""
        # Arrange
        serializer = EditUserAccountSerializer()

        # Act - Nothing to act

        # Assert
        self.assertEqual(serializer.Meta.model, UserAccount)  # Model is correct
        self.assertEqual(serializer.Meta.fields,
                         ['username', 'first_name', 'last_name', 'email', 'avatar'])  # Fields are not changed
        self.assertEqual(serializer.Meta.edit_fields,
                         ['first_name', 'last_name', 'email', 'avatar'])  # Edit fields are not changed
        self.assertEqual(serializer.Meta.read_only_fields,
                         ['username'])  # ReadOnly Fields are not changed
