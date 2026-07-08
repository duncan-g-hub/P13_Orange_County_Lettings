"""Models for the profiles app."""

from django.db import models

from django.contrib.auth.models import User



class Profile(models.Model):
    """Represents a user profile."""
    user = models.OneToOneField(User, on_delete=models.CASCADE)
    favorite_city = models.CharField(max_length=64, blank=True)

    class Meta:
        """Manage plural names."""
        verbose_name = "profile"
        verbose_name_plural = "profiles"

    def __str__(self):
        """Return the username."""
        return self.user.username
