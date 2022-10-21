from django.db import models
from django.contrib.auth.models import AbstractUser

class User(AbstractUser):
	username =models.CharField(max_length=200,unique=True)
	password =models.CharField(max_length=200)

class Menu(models.Model):
	name =models.CharField(max_length =100)
	description =models.TextField()
	price =models.CharField(max_length =10)
	image =models.ImageField(upload_to='image/')

	def __str__(self):
		return self.name 

# Create your models here.