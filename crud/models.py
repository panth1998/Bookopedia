from django.db import models

from User.models import User

# Create your models here.
class Books(models.Model):
    name = models.CharField(max_length=200)
    author = models.CharField(max_length=40)
    price = models.IntegerField()
    description = models.TextField()
    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)

    class Meta():
            db_table = 'Books'

class Demo(models.Model):
    name = models.CharField(max_length=200)
    author = models.CharField(max_length=40)
    price = models.IntegerField()
    description = models.TextField()
    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)

    class Meta():
            db_table = 'Demo'            

class reward(models.Model):
    user_name = models.ForeignKey(User, null=True, on_delete=models.CASCADE, related_name='name')
    book_name = models.ForeignKey(Books, null=True, on_delete=models.CASCADE, related_name='reward_book_name')
    reward_description = models.CharField(max_length=200)
    reward_points = models.IntegerField()
    reward_status = models.BooleanField(default=True)
    reward_created_at = models.DateTimeField(auto_now_add=True)
    reward_updated_at = models.DateTimeField(auto_now=True)
    reward_deleted_at = models.DateTimeField(auto_now=True)

    class Meta:
        db_table = 'reward'