from django.shortcuts import render
from rest_framework import generics,viewsets
from .permissions import IsAuthorOrReadOnly

from students.models import SStudent
from students.serializers import StudentSerializer


# Create your views here.
class StudentsView(viewsets.ModelViewSet):
    queryset = SStudent.objects.all()
    serializer_class = StudentSerializer


class StudentViewusingID(generics.RetrieveUpdateDestroyAPIView):
    permission_classes = (IsAuthorOrReadOnly,)
    queryset = SStudent.objects.all()
    serializer_class = StudentSerializer
