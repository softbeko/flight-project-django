from django.db import models
from django.contrib.auth.base_user import BaseUserManager
from django.contrib.auth.models import AbstractBaseUser, PermissionsMixin


class AppUserManager(BaseUserManager):
    def create_user(self, email, password=None):
        if not email:
            raise ValueError("An email is required.")
        if not password:
            raise ValueError("A password is required.")
        email = self.normalize_email(email)
        user = self.model(email=email)
        user.set_password(password)
        user.save()
        return user

    def create_superuser(self, email, password=None, **extra_fields):
        if not email:
            raise ValueError("An email is required.")
        if not password:
            raise ValueError("A password is required.")
        user = self.model(email=email, **extra_fields)
        user.set_password(password)
        email = self.normalize_email(email)
        user.is_superuser = True
        user.is_staff = True
        user.save(using=self._db)
        return user


class AppUser(AbstractBaseUser, PermissionsMixin):
    user_id = models.AutoField(primary_key=True)
    email = models.EmailField(max_length=50, unique=True)
    username = models.CharField(max_length=50)
    USERNAME_FIELD = "email"
    REQUIRED_FIELDS = ["username"]
    objects = AppUserManager()
    is_staff = models.BooleanField(default=True)
    is_superuser = models.BooleanField(default=True)

    def __str__(self):
        return self.username
