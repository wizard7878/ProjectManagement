from django.contrib import admin
from . import models
# Register your models here.


class UserAdmin(admin.ModelAdmin):
    list_display = ['id', 'fname', 'lname', 'email', 'is_active']

admin.site.register(models.User, UserAdmin)