import uuid

from django.contrib.auth.models import AbstractUser, UserManager
from django.db import models


class User(AbstractUser):
    username = models.UUIDField(default=uuid.uuid4)
    email = models.EmailField('email address', unique=True)

    USERNAME_FIELD = 'email'
    REQUIRED_FIELDS = ('password',)
