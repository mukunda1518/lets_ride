from django.db import models
from django.contrib.auth.models import AbstractUser

class User(AbstractUser):
    phone_number = models.CharField(max_length=30, unique=True)
    profile_pic = models.TextField(default="https://cdn.zeplin.io/5d0afc9102b7fa56760995cc/assets/05bab6ee-6f73-4e37-b727-179336e41690.svg")

