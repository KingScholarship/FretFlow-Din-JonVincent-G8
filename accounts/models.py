from django.contrib.auth.models import AbstractUser
from django.db import models


class CustomUser(AbstractUser):
    class Role(models.TextChoices):
        MEMBER = 'member', 'Member'
        ADMIN = 'admin', 'Admin'

    email = models.EmailField('email address', unique=True)
    role = models.CharField(max_length=10, choices=Role.choices, default=Role.MEMBER)
    display_name = models.CharField(max_length=80, blank=True)
    contact_number = models.CharField(max_length=30, blank=True)

    def __str__(self):
        return self.username
