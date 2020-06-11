from django.db import models

# Create your models here.
class AddPlant(models.Model):
	photo = models.ImageField(upload_to='images/')
	name = models.CharField(max_length=200)
	price = models.IntegerField()
	description = models.TextField()
	u_name = models.CharField(max_length=50,default=None)

	def __str__(self):
		return self.name

