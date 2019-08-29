from django.db import models
from paradigrams.models import Paradigram

# Create your models here.

class Language(models.Model):
	name     = models.CharField(max_length = 50)
	paradigm = models.ForeignKey(Paradigram, on_delete = models.CASCADE)

	def __str__(self):
		return self.name