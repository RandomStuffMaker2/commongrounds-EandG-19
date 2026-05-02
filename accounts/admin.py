from django.contrib import admin
from django.contrib import auth
from django.contrib.auth.admin import UserAdmin
from django.contrib.auth.models import User
from .models import Profile
# Register your models here.

class ProfileInLine(admin.StackedInline):
    model = Profile
    can_delete = False

class UserAdmin(auth.admin.UserAdmin):
    inlines = [ProfileInLine,]

admin.site.unregister(User)
admin.site.register(User, UserAdmin)