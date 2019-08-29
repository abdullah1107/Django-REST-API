from .models import Paradigram
from rest_framework import serializers


class ParadigramSerializer(serializers.ModelSerializer):
	
	class Meta:
		model  = Paradigram
		fields = ('id', 'name')