from __future__ import unicode_literals

from django.db import models
from django.contrib.auth.models import User

from django.utils.encoding import python_2_unicode_compatible
# Create your models here.

@python_2_unicode_compatible  # only if you need to support Python 2
class Category(models.Model):
	name = models.CharField(max_length=100)
	
	def __str__(self):
        	return self.name

class Tag(models.Model):
	name = models.CharField(max_length=100)
	def __str__(self):
        	return self.name

class Post(models.Model):
	title = models.CharField(max_length=20)
	
	body  = models.TextField()
	
	created_time = models.DateTimeField()
	modified_time = models.DateTimeField()
	
	excerpt = models.CharField(max_length=200, blank=True)
	
	category = models.ForeignKey(Category)
	tags     = models.ManyToManyField(Tag)
	author	 = models.ForeignKey(User)

	
	def __str__(self):
        	return self.title
