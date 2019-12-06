from books.models import Book
from rest_framework.generics import ListAPIView
#from django.shortcuts import render
from rest_framework import status
from rest_framework.response import Response
from rest_framework.decorators import api_view, permission_classes
from rest_framework.permissions import IsAuthenticated
from rest_framework.authentication import TokenAuthentication
from rest_framework.pagination import PageNumberPagination
from rest_framework.generics import ListAPIView
from rest_framework.filters import SearchFilter, OrderingFilter
from books.apibooks.serializers import  BookSerializer,BookUpdateSerializer,BookCreateSerializer
##############################
SUCCESS = 'success'
ERROR = 'error'
DELETE_SUCCESS = 'deleted'
UPDATE_SUCCESS = 'updated'
CREATE_SUCCESS = 'created'

@api_view(['DELETE',])
#@permission_classes((IsAuthenticated, ))
def api_delete_book_view(request, pk):

	try:
		info_user = Personal.objects.get(pk=pk)
	except Personal.DoesNotExist:
		return Response(status=status.HTTP_404_NOT_FOUND)


	if request.method == 'DELETE':
		operation = info_user.delete()
		data = {}
		if operation:
			data['response'] = DELETE_SUCCESS
		return Response(data=data)

@api_view(['PUT'])
def api_update_book_view(request,pk):

	try:
		info_book = Book.objects.get(pk=pk)
		#print (info_user.image_file)
	except Book.DoesNotExist:
		return Response(status=status.HTTP_404_NOT_FOUND)

	if request.method == 'PUT':
		serializer = BookUpdateSerializer(info_book, data=request.data, partial=True)
		data = {}
		if serializer.is_valid():
			serializer.save()
			# data['response'] = UPDATE_SUCCESS
			# data['pk'] = info_user.pk
			# data['first_name']=info_user.first_name
			# data['last_name'] = info_user.last_name
			# data['blood_gp'] = info_user.blood_gp
			return Response(data=data)
		return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)


@api_view(['POST'])
def api_create_book_view(request):

	if request.method == 'POST':
		print("inside create method!!!!!")
		data = request.data
		print(data)
		serializerboard = BookCreateSerializer(data=data)
		print(serializerboard)

		data = {}
		if serializerboard.is_valid():
			info = serializerboard.save()
			print("information", info)
			data['response'] = CREATE_SUCCESS
			data['pk'] = info.pk
			# data['first_name'] = info.first_name
			# data['last_name'] = info.last_name
			# data['blood_gp'] = info.blood_gp
			# data['gender']   = info.gender
			# data['contact_number'] = info.contact_number
			# data['email']  = info.email
			# data['group_number'] = info.group_number
			return Response(data=data)
		return Response(serializerboard.errors, status=status.HTTP_400_BAD_REQUEST)

class  BookListView(ListAPIView):
	queryset = Book.objects.all()
	serializer_class = BookSerializer
	pagination_class = PageNumberPagination
	filter_backends = (SearchFilter, OrderingFilter)
	search_fields = ('book_name')
