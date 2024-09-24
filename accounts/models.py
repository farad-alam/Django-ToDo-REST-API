import random
from django.contrib.auth.models import AbstractBaseUser, BaseUserManager, PermissionsMixin, AbstractUser
from django.db import models
from django.utils import timezone

class CustomUserManager(BaseUserManager):
    def create_user(self, email, password=None, **extra_fields):
        if not email:
            raise ValueError("The Email field must be set")
        
        email = self.normalize_email(email)
        user = self.model(email=email, **extra_fields)
        
        # Auto-generate username
        first_name = extra_fields.get('first_name', '')
        last_name = extra_fields.get('last_name', '')
        user.username = self.generate_unique_username(first_name, last_name)

        # Hash the password
        user.set_password(password)
        user.save(using=self._db)
        return user

    def create_superuser(self, email, password=None, **extra_fields):
        extra_fields.setdefault('is_staff', True)
        extra_fields.setdefault('is_superuser', True)
        extra_fields.setdefault('first_name', 'Admin')  # Set a default first name for superuser
        return self.create_user(email=email, password=password, **extra_fields)
    
    
    def generate_unique_username(self, first_name, last_name):
        base_username = f"{first_name.lower().replace(' ', '')}.{last_name.lower().replace(' ', '')}" if last_name else first_name.lower()
        username = base_username or "user"
        while CustomUser.objects.filter(username=username).exists():
            username = f"{base_username}{random.randint(1000, 9999)}"
        return username


# class CustomUser(AbstractBaseUser, PermissionsMixin):
class CustomUser(AbstractBaseUser, PermissionsMixin):
    first_name = models.CharField(max_length=30)
    last_name = models.CharField(max_length=30, blank=True, null=True)
    email = models.EmailField(unique=True)
    username = models.CharField(max_length=150, unique=True)
    # username = None
    phone_number = models.CharField(max_length=15, blank=True, null=True)
    is_active = models.BooleanField(default=True)
    is_staff = models.BooleanField(default=False)  # User can be staff or admin
    date_joined = models.DateTimeField(default=timezone.now)
    last_updated = models.DateTimeField(auto_now=True)

    objects = CustomUserManager()

    USERNAME_FIELD = 'email'
    REQUIRED_FIELDS = ['first_name']

    def __str__(self):
        return self.email
