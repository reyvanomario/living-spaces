from django.db import models
import uuid

# Create your models here.
from django.db import models

class Product(models.Model):
    id = models.UUIDField(primary_key=True, default=uuid.uuid4, editable=False)
    name = models.CharField(max_length=40)
    price = models.IntegerField()
    description = models.TextField()
    stock = models.IntegerField()
    category = models.CharField(max_length=15)
    

    
