from django.shortcuts import render
from rest_framework import viewsets
from .models import Paradigram
from .serializers import ParadigramSerializer

# Create your views here.

class ParadigramView(viewsets.ModelViewSet):
	queryset = Paradigram.objects.all()
	serializer_class = ParadigramSerializer