from django.shortcuts import render
from rest_framework import viewsets
from courses.models import MyCourse
from courses.serializers import CourseSerializer

# Create your views here.
class CourseView(viewsets.ModelViewSet):
    queryset = MyCourse.objects.all()
    serializer_class = CourseSerializer
