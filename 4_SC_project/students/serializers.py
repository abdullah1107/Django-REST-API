from rest_framework import serializers
from students.models import SStudent


class StudentSerializer(serializers.ModelSerializer):
    class Meta:
        model = SStudent
        fields = ('id', 'advisor', 'user_name', 'first_name', 'last_name', 'email')
