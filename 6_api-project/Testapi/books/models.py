from django.db import models
from personalinfo.models import Personal

# Create your models here.
class Book(models.Model):

	book_name 				= models.CharField(max_length=50, null=False, blank=True)
	category                = models.CharField(max_length=50, null=False, blank=True)
	#book_file               = models.FileField(null =False, blank=True),
	personid                = models.ForeignKey(Personal,related_name='personalinfo', on_delete=models.CASCADE, blank=True)


	def __str__(self):
		return self.book_name
