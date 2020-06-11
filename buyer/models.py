from django.db import models

# Create your models here.
class Cart(models.Model):
	pic = models.ImageField(upload_to='images')
	name = models.CharField(max_length=100)
	price = models.IntegerField()
	us = models.CharField(max_length=100)
	seller_us=models.CharField(max_length=100,default=None)
class Checkout(models.Model):
	fname = models.CharField(max_length=100)
	lname = models.CharField(max_length=100)
	email = models.CharField(max_length=200)
	phone = models.CharField(max_length=15)
	address = models.CharField(max_length=400)
	town = models.CharField(max_length=100)
	state = models.CharField(max_length=100)
	country = models.CharField(max_length=100)
	order_notes = models.TextField()
	use = models.CharField(max_length=100)
	seller_use = models.CharField(max_length=100,default=None)
	product_name = models.CharField(max_length=200,default=None)


