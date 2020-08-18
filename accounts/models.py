import uuid

from django.contrib.auth.models import AbstractUser, UserManager
from django.db import models


def is_valid_uuid(val):
    try:
        uuid.UUID(str(val))
        return True
    except ValueError:
        return False


class CustomUserManager(UserManager):
    def create_user(self, username=None, email=None, password=None, **extra_fields):
        if username is None or not is_valid_uuid(username):
            username = uuid.uuid4()
        return super().create_user(username, email, password, **extra_fields)

    def create_superuser(self, username=None, email=None, password=None, **extra_fields):
        if username is None or not is_valid_uuid(username):
            username = uuid.uuid4()
        return super().create_superuser(username, email, password, **extra_fields)


class User(AbstractUser):
    email = models.EmailField('email address', unique=True)

    USERNAME_FIELD = 'email'
    REQUIRED_FIELDS = ('password',)

    objects = CustomUserManager()

    def save(self, *args, **kwargs):
        if self.username is None or not is_valid_uuid(self.username):
            self.username = uuid.uuid4()
        super().save(*args, **kwargs)
