from django.db import models
from django.contrib.auth.models import AbstractUser


class User(AbstractUser):
    user_id = models.TextField(
        verbose_name='User id',
        max_length=64,
        null=True,
        blank=True
    )

    def __str__(self):
        return 'Authorized'