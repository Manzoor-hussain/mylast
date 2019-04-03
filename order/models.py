from django.db import models

# Create your models here.
from django.contrib.auth.models import Permission, User


# Create your models here.
from django.db import models
from datetime import datetime


class Seller(models.Model):
    user_key= models.ForeignKey(User, on_delete=models.CASCADE)
    catagory=models.CharField(max_length=100)
    product_name=models.CharField(max_length=100)
    product_quality=models.CharField(max_length=100)
    product_quentity=models.CharField(max_length=100)
    product_shiping=models.CharField(max_length=50)
    product_price=models.IntegerField()
    description=models.TextField()
    product_image=models.ImageField(upload_to='product_pictures')

    province=models.CharField(max_length=100)
    city= models.TextField(max_length=200)

    created_at =models.DateTimeField(default=datetime.now, blank=True)
    latitude = models.FloatField(blank=False, default=0)
    langitude = models.FloatField(blank=False, default=0)



class Buyer(models.Model):
    user_key= models.ForeignKey(User, on_delete=models.CASCADE)
    catagory=models.CharField(max_length=100)
    product_name=models.CharField(max_length=100)
    product_quality=models.CharField(max_length=100)
    product_quentity=models.CharField(max_length=100)
    product_shiping=models.CharField(max_length=50)
    product_price=models.IntegerField()
    description=models.TextField()
    product_image=models.ImageField(upload_to='buyer/product_pictures')
    province=models.CharField(max_length=100)
    city= models.CharField(max_length=100)
    created_at =models.DateTimeField(default=datetime.now, blank=True)
    latitude = models.DecimalField(max_digits=2, decimal_places=2, blank=True, default=0)
    langitude = models.DecimalField(max_digits=2, blank=True, decimal_places=2, default=0)






class Customer(models.Model):
    user_key= models.ForeignKey(User, on_delete=models.CASCADE)
    catagory=models.CharField(max_length=200 )
    product_name=models.CharField(max_length=200)
    product_quality=models.CharField(max_length=100)
    product_quentity=models.CharField(max_length=100)
    product_shiping=models.CharField(max_length=50)
    product_price=models.IntegerField()
    description=models.TextField()
    product_image=models.ImageField(upload_to='product_pictures')
    product_image_one= models.ImageField(upload_to='product_pictures_two')

    province=models.CharField(max_length=100)
    city= models.TextField(max_length=300)

    created_at =models.DateTimeField(default=datetime.now, blank=True)
    latitude = models.CharField(max_length=100)
    langitudee = models.CharField(max_length=100)
    customer=models.CharField(max_length=100)
    expire=models.CharField(max_length=100)
class Manzoor(models.Model):
    name=models.CharField(max_length=100)
class Khan(models.Model):
    user_key= models.ForeignKey(User, on_delete=models.CASCADE)
    catagory=models.CharField(max_length=200 )
    product_name=models.CharField(max_length=200)
    product_quality=models.CharField(max_length=100)
    product_quentity=models.CharField(max_length=100)
    product_shiping=models.CharField(max_length=50)
    product_price=models.IntegerField()
    description=models.TextField()
    product_image=models.ImageField(upload_to='product_pictures')
    product_image_one= models.ImageField(upload_to='product_pictures_two')

    province=models.CharField(max_length=100)
    city= models.TextField(max_length=300)

    created_at =models.DateTimeField(default=datetime.now, blank=True)
    latitude = models.CharField(max_length=100)
    langitudee = models.CharField(max_length=100)
    customer=models.CharField(max_length=100)
    expire=models.CharField(max_length=100)
