from rest_framework import serializers
from .models import MyCourse


class CourseSerializer(serializers.ModelSerializer):
    class Meta:
        model  = MyCourse
        fields = ('id', 's_id', 'course_name', 'description','start_date')
