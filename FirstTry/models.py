from django.db import models

class Person(models.Model):
	first_name = models.CharField(max_length=30)
	last_name = models.CharField(max_length=30)
	age = models.CharField(max_length=3)
	about_me = models.TextField()

	def __unicode__(self):
		return self.first_name

class Favourite(models.Model):
	info = models.ForeignKey(Person)
	Color = models.CharField(max_length=30)
	Food = models.CharField(max_length=50)
	State = models.CharField(max_length=50)
	Country = models.CharField(max_length=50)
	Human = models.TextField()

	def __unicode__(self):
		return self.Color
