from django.db import models
from apps.users.models import User

class Category(models.Model):

	name = models.CharField(max_length=50)

	def __unicode__(self):
		return self.name

class City(models.Model):

	name = models.CharField(max_length=50)

	def __unicode__(self):
		return self.name

class Restaurant(models.Model):	

	category = models.ManyToManyField(Category)
	name = models.CharField(max_length=50)
	description = models.TextField(max_length=50)

	def __unicode__(self):
		return self.name

class Establishment(models.Model):
	city = models.ForeignKey(City)
	restaurant = models.ForeignKey(Restaurant)
	address = models.CharField(max_length=50)

	def __unicode__(self):
		return self.restaurant.name

class Comments(models.Model):

	user = models.ForeignKey(User)
	restaurant = models.ForeignKey(Restaurant)
	content = models.TextField(max_length=200)