from rest_framework import serializers
from personalinfo.models import Personal
from django.core.files.storage import default_storage
from django.core.files.storage import FileSystemStorage
from books.models import Book
from books.apibooks.serializers import BookSerializer

class PersonalUpdateSerializer(serializers.ModelSerializer):

	class Meta:
		model = Personal
		fields = ('pk','first_name', 'last_name', 'blood_gp', 'image_file')

class PersonalSerializer(serializers.ModelSerializer):
	personalinfo = BookSerializer(many=True)
	class Meta:
		model = Personal
		fields = ('pk','first_name','last_name', 'blood_gp', 'gender', 'contact_number', 'email', 'group_number','image_file','personalinfo')

class  PersonalCreateSerializer(serializers.ModelSerializer):
	class Meta:
		model = Personal
		fields = ('first_name','last_name', 'blood_gp', 'gender', 'contact_number', 'email', 'group_number','image_file')

	def save(self):
		try:
			first_name         = self.validated_data['first_name']
			last_name          = self.validated_data['last_name']
			blood_gp           = self.validated_data['blood_gp']
			gender             = self.validated_data['gender']
			contact_number     = self.validated_data['contact_number']
			email              = self.validated_data['email']
			group_number       = self.validated_data['group_number']
			image_file         = self.validated_data['image_file']
			personalinfo = Personal(
								first_name=first_name,
								last_name=last_name,
								blood_gp=blood_gp,
								gender= gender,
								contact_number = contact_number,
								email = email,
								group_number =group_number,
								image_file =image_file
								)
			personalinfo.save()
			return personalinfo
		except KeyError:
			raise serializers.ValidationError({"response": "this invalid somethings!!!!!"})