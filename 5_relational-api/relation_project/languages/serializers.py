from .models import Language
from rest_framework import serializers


class LanguageSerializer(serializers.ModelSerializer):
	class Meta:
		model  = Language
		fields = ('id', 'name', 'paradigm')