from django.db import models
from django.contrib.auth.models import User


class Profile(models.Model):
    class Role(models.TextChoices):
        MEMBER = 'member', 'Member'
        ADMIN = 'admin', 'Admin'

    user = models.OneToOneField(User, on_delete=models.CASCADE, related_name='profile')
    role = models.CharField(max_length=10, choices=Role.choices, default=Role.MEMBER)
    display_name = models.CharField(max_length=80, blank=True)
    contact_number = models.CharField(max_length=30, blank=True)

    def __str__(self):
        return f'{self.user.username} ({self.role})'
