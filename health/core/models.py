"""
Database models
"""

import uuid
import os

from django.db import models
from django.contrib.auth.models import (
    AbstractBaseUser,
    BaseUserManager,
    PermissionsMixin
)
from django.core.validators import RegexValidator

# lets us explicitly set upload path and filename


def user_image_file_path(instance, filename):
    """Generate file path for new user image"""
    ext = os.path.splitext(filename)[1]
    filename = f'{uuid.uuid4()}{ext}'

    return os.path.join('media', 'user', filename)


class UserManager(BaseUserManager):
    """manager for users."""

    def create_user(self, email, password=None, **extra_Field):
        """create , save and return new user"""
        if not email:
            raise ValueError("User must have an email address")
        user = self.model(email=self.normalize_email(email), **extra_Field)
        user.set_password(password)
        user.save(using=self._db)

        return user

    def create_superuser(self, email, password):
        """create and return new superuser"""
        user = self.create_user(email, password)
        user.is_staff = True
        user.is_superuser = True
        user.save(using=self._db)

        return user


class User(AbstractBaseUser, PermissionsMixin):
    """user in the system"""
    email = models.EmailField(max_length=254, unique=True)
    first_name = models.CharField(max_length=50)
    last_name = models.CharField(max_length=255, blank=True)
    is_active = models.BooleanField(default=True)
    is_staff = models.BooleanField(default=False)
    created_at = models.DateTimeField(auto_now_add=True, editable=False)
    updated_at = models.DateTimeField(
        auto_now=True, auto_now_add=False)
    address = models.CharField(max_length=50, default='')
    phone_regex = RegexValidator(
        regex=r'^\+?1?\d{9,15}$',
              message="Phone number must be entered \
                in the format: '+999999999'. Up to 15 digits allowed.")
    phone_number = models.CharField(
        validators=[phone_regex], max_length=17,
        blank=True, default='')  # Validators should be a list
    image = models.ImageField(null=True, upload_to=user_image_file_path)

    objects = UserManager()

    USERNAME_FIELD = 'email'
