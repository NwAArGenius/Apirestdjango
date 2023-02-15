from django.db import models
from django.contrib.auth.models import AbstractUser
from django.contrib.auth.base_user import BaseUserManager
# Create your models here.
class CustumUserManage(BaseUserManager):
    def create_user(self, email, password, **extrs_fields):
        email = self.normalize_email(email)
        user = self.model(
            email=email,
            **extrs_fields
        )
        user.set_password(password)
        user.save()
        return user
    
    def create_superuser(self, email, password, **extra_fields):
        extra_fields.setdefault("is_staff",True)
        extra_fields.setdefault("is_superuser", True)
        
        if extra_fields.get("is_staff") is not True:
            raise ValueError("error in is staff")
        if extra_fields.get("is_superuser") is not True:
            raise ValueError("is_superuser")
        return self.create_user(email=email, password=password, **extra_fields)
    
class User(AbstractUser):
    email = models.CharField(max_length=50, unique=True)
    username = models.CharField(max_length=50)
    date_of_birth = models.DateField(null=True)
    
    object = CustumUserManage()
    USERNAME_FIELD = "email"
    REQUIRED_FIELDS = ["username"]
    
    def __str__(self):
        return self.username