from django.contrib.auth.models import AbstractUser
from django.db import models


class UserAccount(AbstractUser):
    """
    Class that represents a user account.
    """
    # Other fields inherited from AbstractUser
    avatar = models.ImageField(help_text='User avatar')
