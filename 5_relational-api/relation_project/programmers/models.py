from django.db import models
from languages.models import Language

# Create your models here.
class Programmar(models.Model):
	name     = models.CharField(max_length = 50)
	language = models.ManyToManyField(Language)

	def __str__(self):
		return self.name

