from django.db import models
import uuid
from django.contrib.auth.models import User

# Create your models here.



class Product(models.Model):
    id = models.UUIDField(primary_key=True, default=uuid.uuid4, editable=False)
    user = models.ForeignKey(User, on_delete=models.CASCADE)
    name = models.CharField(max_length=40)
    price = models.IntegerField()
    description = models.TextField()
    stock = models.IntegerField()
    category = models.CharField(max_length=15)


class Person(models.Model):
    name = models.CharField(max_length=40)
    age = models.IntegerField()
    is_happy = models.BooleanField()
    

    
