from django.contrib.auth.models import AbstractUser
from django.db import models



class User(AbstractUser):
    username = models.CharF
    phone_number = models.CharField(max_length=20)
    profile_pic = models.TextField()

