from django.db import models


class UserAccount(models.Model):
    """
    Class that represents a user account.
    """
    first_name = models.CharField(help_text='First name of the user')
    last_name = models.CharField(help_text='Last name of the user')
    email = models.EmailField(help_text='Email of the user')
    password = models.CharField(help_text='Password of the user')
    avatar = models.ImageField(help_text='User avatar')

    @property
    def name(self):
        """Full name of the user"""
        return f'{self.first_name} {self.last_name}'
