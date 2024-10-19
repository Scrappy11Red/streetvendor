from django.db import models
from django.contrib.auth.models import AbstractUser

# Create your models here.
class User(AbstractUser):
    username = models.CharField(max_length=125, unique=True)
    email = models.EmailField(("email address"), unique=True)
    password = models.CharField(max_length=50)

    def __str__(self):
        return self.username