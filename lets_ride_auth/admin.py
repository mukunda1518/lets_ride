from django.contrib import admin
from django.contrib.auth.admin import UserAdmin
from lets_ride_auth.models.user import User


admin.site.register(User, UserAdmin)
