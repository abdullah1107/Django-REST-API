from .models import Programmar
from rest_framework import serializers


class ProgrammerSerializer(serializers.ModelSerializer):
	class Meta:
		model  = Programmar
		fields = ('id', 'name', 'language')