from django.contrib import admin
from django.contrib.auth.admin import UserAdmin
from .models import User


class CustomUserAdmin(UserAdmin):
    # admin panelde bunlar görünsün
    list_display = ('id', 'username', 'email', 'role')


admin.site.register(User, CustomUserAdmin)



