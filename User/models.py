from django.db import models
from django.contrib.auth.models import AbstractUser
from django.core.validators import  RegexValidator

#from generic.models import BaseField

# Creae your models here.
class User(AbstractUser):
    username = models.CharField(max_length = 99, unique = True)
    firstname = models.CharField(max_length = 99)
    lastname = models.CharField(max_length = 99,null=True, blank=True,default="")
    email = models.EmailField(max_length=150, unique=True)
    phone_regex = RegexValidator(regex=r'^[6-9]{1}\d{9}', message="Phone number must be entered in the format: '999999999'")
    phone_number = models.CharField(validators=[phone_regex], max_length=10, blank=True, unique=True) 
    gender=models.CharField(max_length = 10)
    created_at = models.DateTimeField(auto_now_add = True)
    updated_at = models.DateTimeField(auto_now = True)
    is_deleted = models.BooleanField(default=False)
    USERNAME_FIELD = 'username'
    REQUIRED_FIELDS = ['email']
    
    
    class Meta:
        db_table = "User"

    def _str_(self):
        return self.username