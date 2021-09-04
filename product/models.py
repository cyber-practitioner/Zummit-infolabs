from django.db import models
from django.utils import timezone
# Create your models here.
class order(models.Model):
    customer_id=models.CharField(max_length=100,primary_key=True)
    category =models.CharField(max_length=100)
    order_id=models.CharField(max_length=300)
    date_purchased=models.DateField(default=timezone.now)

class products(models.Model):
    product_id=models.CharField(max_length=100)
    product_weight=models.CharField(max_length=100)
    category =models.CharField(max_length=100)
    price=models.IntegerField()
    customer_id_who_purchased=models.CharField(max_length=100,primary_key=True)


class consumer(models.Model):
    customer_id=models.CharField(max_length=100,primary_key=True)
    namez=models.CharField(max_length=100)
    city=models.CharField(max_length=100)
    state=models.CharField(max_length=100)
    mode_of_payment=models.CharField(max_length=100)

class users(models.Model):
    customer_id=models.CharField(max_length=100,primary_key=True)
    uname=models.CharField(max_length=100)
    password=models.CharField(max_length=100)
    



  