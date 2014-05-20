from django.db import models

class City(models.Model):
	description = models.CharField(max_length=128)
	uf = models.CharField(max_length=2)

	def __unicode__(self): 
		return self.description 


class Menu(models.Model):
	description = models.CharField(max_length=128)
	active = models.NullBooleanField(default=False)
	members = models.ManyToManyField(City, through='CityMenu')

	def __unicode__(self):
		return self.description

class Local(models.Model):
	name = models.CharField(max_length=255)
	telephone = models.CharField(max_length=16)
	site = models.CharField(max_length=255)
	email = models.CharField(max_length=255)
	description = models.CharField(max_length=1000)
	address = models.CharField(max_length=255)
	latitude = models.CharField(max_length=20)
	longitude = models.CharField(max_length=20)
	active = models.BooleanField()
	pathImage = models.CharField(max_length=255)
	date = models.DateTimeField()
	menu = models.ForeignKey(Menu)
	city = models.ForeignKey(City)
	

class CityMenu(models.Model):
	city = models.ForeignKey(City)
	menu = models.ForeignKey(Menu)
	date = models.DateTimeField()
	active = models.BooleanField()


class Image(models.Model):
	name = models.CharField(max_length=255)


class Comment(models.Model):
	rating = models.FloatField()
	description = models.CharField(max_length=1000)
	date = models.DateTimeField()
	active = models.BooleanField()
	local = models.ForeignKey(Local)


class User(models.Model):
	email = models.CharField(max_length=100)
	password = models.CharField(max_length=100)
	name = models.CharField(max_length=100)
	lastName = models.CharField(max_length=100)
