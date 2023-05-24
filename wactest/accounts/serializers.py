from drf_extra_fields.fields import Base64ImageField
from rest_framework.serializers import ModelSerializer

from accounts.models import UserAccount


class ReadUserAccountSerializer(ModelSerializer):
    avatar = Base64ImageField()

    class Meta:
        model = UserAccount
        fields = ['username', 'first_name', 'last_name', 'email', 'avatar']
        read_only_fields = fields
    #
    # def get_avatar(self, user_account):
    #     return base64.b64encode(user_account.avatar.file.read())


class EditUserAccountSerializer(ModelSerializer):
    avatar = Base64ImageField()

    class Meta:
        model = UserAccount
        fields = ['username', 'first_name', 'last_name', 'email', 'avatar']
        edit_fields = ['first_name', 'last_name', 'email', 'avatar']
        read_only_fields = list(set(fields) - set(edit_fields))

