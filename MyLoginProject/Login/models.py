from MyLoginProject.settings import PASSWORD_HASHERS
from django.db import models
from django.contrib.auth.hashers import make_password
# Create your models here.
class Login(models.Model):
    email=models.EmailField(max_length=122)
    password=models.TextField(max_length=122)
    is_super_user=models.BooleanField(default=False)
