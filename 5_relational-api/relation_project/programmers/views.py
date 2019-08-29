from django.shortcuts import render
from rest_framework import viewsets
from .models import Programmar
from .serializers import ProgrammerSerializer

# Create your views here.

class ProgrammerView(viewsets.ModelViewSet):
	queryset = Programmar.objects.all()
	serializer_class = ProgrammerSerializer

