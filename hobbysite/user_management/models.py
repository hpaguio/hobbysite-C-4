from django.db import models
from django.contrib.auth.models import User


class Profile(models.Model):
    """
    Extends the built-in Django User model with additional profile information.
    """
    user = models.OneToOneField(User, on_delete=models.CASCADE, related_name="profile")
    display_name = models.CharField(max_length=63)
    email = models.EmailField()

    def __str__(self):
        return self.display_name or self.user.username

    class Meta:
        ordering = ["display_name"]
        verbose_name = "Profile"
        verbose_name_plural = "Profiles"