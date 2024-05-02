from django.db import models
from django.contrib.auth.models import AbstractUser
from django.core.validators import  RegexValidator



# Create your models here.
class author(models.Model):
    author_name = models.CharField(max_length=99)

    class meta:
        db_table = 'author'


class book(models.Model):
    name = models.CharField(max_length=99)
    book_price = models.IntegerField()
    author_id = models.ForeignKey(author,on_delete=models.CASCADE )
    #user_id = models.ForeignKey(User, on_delete=models.CASCADE)
    ischarity = models.BooleanField(default=False)

    class meta:
        db_table = "book"