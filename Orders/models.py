from django.db import models

# Create your models here.

class Order(models.Model):
    related_customer_name = models.CharField(max_length=100, verbose_name="Customer Name")
    address = models.TextField(verbose_name="Address")
    phone_number = models.CharField(max_length=350,verbose_name="Phone Number")
    #related_products = models.ManyToManyField(Cart, verbose_name="Related products")