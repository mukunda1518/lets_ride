from django.contrib import admin
from django.contrib.auth.admin import UserAdmin
from reporting_portal.models.observation import User


admin.site.register(User, UserAdmin)