from django.db import models
from django.contrib.auth.models import Permission, User


# Create your models here.
from django.db import models
from datetime import datetime

# Create your models here.
class Customerr(models.Model):
    user_key= models.ForeignKey(User, on_delete=models.CASCADE)
    catagory=models.CharField(max_length=200,null=True)
    product_name=models.CharField(max_length=200,null=True)
    product_quality=models.CharField(max_length=100,null=True)
    product_quentity=models.CharField(max_length=100,null=True)
    product_shiping=models.CharField(max_length=50,null=True)
    product_price=models.IntegerField()
    description=models.TextField(max_length=300,null=True)
    product_image=models.ImageField(upload_to='product_pictures',null=True)
    product_image_one= models.ImageField(upload_to='product_pictures_two',null=True)
    province=models.CharField(max_length=100,null=True)
    city= models.TextField(max_length=300,null=True)
    created_at =models.DateTimeField(default=datetime.now, blank=True)
    latitude = models.FloatField(blank=False, default=0)
    langitude = models.FloatField(blank=False, default=0)
    type=models.CharField(max_length=100,null=True)
    expire=models.CharField(max_length=100,null=True)
    last_name=models.CharField(max_length=100,null=True)

class Naveed(models.Model):
    name=models.CharField(max_length=100)
