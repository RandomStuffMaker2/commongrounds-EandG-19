from django.db import models
from django.urls import reverse
from django.contrib.auth.models import User

# Create your models here.

class Profile(models.Model):
    user = models.OneToOneField(
        User,
        on_delete=models.CASCADE,
        related_name='profile'
    )
    displayName = models.CharField(max_length=50)
    email = models.EmailField(unique=True)

    def get_absolute_url(self):
        return reverse('accounts:profileupdate', kwargs={'displayName': self.displayName})