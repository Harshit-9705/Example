from django.db import models
from .managers import *
# Create your models here.
from django.contrib.auth.models import AbstractUser

class CustomUser(AbstractUser):
    phone_num = models.CharField(max_length=100,unique=True)
    username = None

    USERNAME_FIELD = "phone_num"
    REQUIRED_FIELDS = []

    objects = CustomManagers()


# from django.db import models
# from django.contrib.auth.models import AbstractUser
# from .managers import CustomUserManager

# class CustomUser(AbstractUser):
#     phone_num = models.CharField(max_length=100, unique=True)
#     username = None  # Disable username field

#     USERNAME_FIELD = 'phone_num'
#     REQUIRED_FIELDS = []  # No additional fields required for createsuperuser

#     objects = CustomUserManager()  # Assign custom manager
