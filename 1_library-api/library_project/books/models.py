from django.db import models

# Create your models here.


class Book(models.Model):

	title     = models.CharField(max_length = 150)
	sub_title = models.CharField(max_length = 120)
	author    = models.CharField(max_length = 100)
	isbn      = models.CharField(max_length = 20)


	def __str__(self):
		return self.title
