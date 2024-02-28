from django.db import models
from django.conf import settings
from django.contrib.auth.models import (
    AbstractBaseUser,
    BaseUserManager,
    PermissionsMixin
)
import os, uuid

# Create your models here.
def avatar_image_file_path(instance, filename):
    """user avatar location"""
    
    ext = filename.split('.')[-1]
    filename = f'{uuid.uuid4()}.{ext}'
    return os.path.join('uploads/avatars/', filename) 

class UserManager(BaseUserManager):
    def create_user(self, email, password=None, **extra_fields):
        """ create user function for custom user model"""
        if not email:
            raise ValueError("Email is Required!")
        user = self.model(email = self.normalize_email(email))
        user.set_password(password)
        user.save(using=self._db)
        return user
    
    def create_superuser(self,email, password=None, **extra_fields):
        """ create superuser function for custom user model"""
        user = self.create_user(email=email, password=password)
        user.is_staff = True
        user.is_superuser  = True
        user.save(using=self._db)
        return user

class User(AbstractBaseUser, PermissionsMixin):
    """User Model fields"""
    email = models.EmailField(max_length=255, unique=True)
    fname = models.CharField(max_length=255)
    lname = models.CharField(max_length=255)
    phonenumber = models.CharField(max_length=11, unique=True, null=True) 
    avatar = models.ImageField(upload_to=avatar_image_file_path, null=True)
    is_active = models.BooleanField(default=True)
    is_staff = models.BooleanField(default=False)
    password = models.CharField(max_length=100)

    objects = UserManager()

    USERNAME_FIELD = 'email'

    def __str__(self) -> str:
        return self.fname +  '  ' + self.lname
    