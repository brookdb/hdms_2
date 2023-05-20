from django.db import models
from django.contrib.auth.base_user import BaseUserManager
from django.contrib.auth.models import AbstractBaseUser, PermissionsMixin
from django.utils.text import slugify
from django.utils import timezone
from django.utils.translation import gettext as _
import binascii


GENDER_CHOICES = [
    ('M', 'Male'),
    ('F', 'Female'),
    ('O', 'Other')
]

class CustomUserManager(BaseUserManager):
    def create_user(self, email, password=None, **extra_fields):
        if not email:
            raise ValueError('An email is required.')
        if not password:
            raise ValueError('A password is required.')
        email = self.normalize_email(email)
        user = self.model(email=email, **extra_fields)
        user.set_password(password)
        user.save()
        return user

    def create_superuser(self, email, password=None, **extra_fields):
        extra_fields.setdefault("is_staff", True)
        extra_fields.setdefault("is_superuser", True)
        extra_fields.setdefault("is_active", True)

        if extra_fields.get("is_staff") is not True:
            raise ValueError("Superuser must have is_staff=True.")
        if extra_fields.get("is_superuser") is not True:
            raise ValueError("Superuser must have is_superuser=True.")
        return self.create_user(email, password, **extra_fields)

class CustomUser(AbstractBaseUser, PermissionsMixin):
    email = models.EmailField(_("email address"), unique=True)
    is_staff = models.BooleanField(default=False)
    is_active = models.BooleanField(default=True)
    date_joined = models.DateTimeField(default=timezone.now)

    USERNAME_FIELD = "email"
    REQUIRED_FIELDS = []

    objects = CustomUserManager()
    first_name = models.CharField(max_length=200, unique=True)
    last_name = models.CharField(max_length=200, unique=True)
    gender = models.CharField(choices=GENDER_CHOICES, max_length=1, blank=True)
    slug = models.SlugField(max_length=200, unique=True)
    dob = models.DateTimeField(default=timezone.now)
    updated_on = models.DateTimeField(auto_now=True)
    avatar = models.ImageField(blank=True, null=True, upload_to='media/img/profile/')
    photo_ID = models.ImageField(blank=True, null=True, upload_to='media/img/ID/')
    address_1 = models.CharField(_("address"), max_length=128, blank=True)
    address_2 = models.CharField(_("address cont'd"), max_length=128, blank=True)
    city = models.CharField(_("city"), max_length=64, blank=True)
    state = models.CharField(_("state"), max_length=100, blank=True)
    zip_code = models.CharField(_("zip code"), max_length=5, blank=True)

    class Meta:
        ordering = ['last_name']

    def __str__(self):
        return self.email

    def save(self, *args, **kwargs):
        if not self.slug:
            slug = "USR" + binascii.hexlify(self.email.encode()).decode()
            print(slug)
            self.slug = slugify(slug)
        return super().save(*args, **kwargs)
