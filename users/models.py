from django.db import models
from django.contrib.auth.models import AbstractUser
# Create your models here.
# import blog.models as bg



class User(AbstractUser):
    email = models.EmailField(unique=True, blank=False)
    bio = models.TextField(null=True)
    avatar = models.ImageField(default="avatar.svg", null=True)
    mobile = models.CharField(max_length=13, blank=True, null=True)
    country = models.CharField(max_length=100, blank=True, null=True)
    date_of_birth = models.DateField(blank=True, null=True)
    gender =  models.CharField(max_length=10, blank=True, null=True)

   


    # USERNAME_FIELD = 'email'
    REQUIRED_FIELDS = []
