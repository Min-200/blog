from __future__ import unicode_literals

from django.db import models
from django.contrib.auth.models import User

# Create your models here.


class Category(models.Model):
	name = models.CharField(max_length=100)


class Tag(models.Model):
	name = models.CharField(max_length=100)

class Post(models.Model):
	title = models.CharField(max_length=20)
	
	body  = models.TextField()
	
	created_time = models.DateTimeField()
	modified_time = models.DateTimeField()
	
	excerpt = models.CharField(max_length=200, blank=Ture)
	
	category = models.ForeignKey(Category)
	tags     = models.ManyToManyField(Tag)
	author	 = models.ForeignKey(User)
