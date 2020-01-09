from django.db import models

class registerdata(models.Model):
    fname = models.CharField(max_length=100)
    lname = models.CharField(max_length=100)
    username = models.CharField(max_length=100)
    password = models.CharField(max_length=100)
    email  = models.EmailField(max_length=100)
    mobile = models.BigIntegerField()

class createdata (models.Model):
    product_id = models.IntegerField()
    product_name = models.CharField(max_length=100)
    product_cost = models.IntegerField()
    product_color = models.CharField(max_length=100)
    cust_name = models.CharField(max_length=100)
    cust_mobile = models.BigIntegerField()

