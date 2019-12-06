from personalinfo.models import Personal
from rest_framework.generics import ListAPIView
from django.shortcuts import render
from rest_framework import status
from rest_framework.response import Response
from rest_framework.decorators import api_view, permission_classes
from rest_framework.permissions import IsAuthenticated
from rest_framework.authentication import TokenAuthentication
from rest_framework.pagination import PageNumberPagination
from rest_framework.generics import ListAPIView
from rest_framework.filters import SearchFilter, OrderingFilter
from personalinfo.api.serializers import  PersonalSerializer,PersonalCreateSerializer,PersonalUpdateSerializer
# Create your views here.
##############################
SUCCESS = 'success'
ERROR = 'error'
DELETE_SUCCESS = 'deleted'
UPDATE_SUCCESS = 'updated'
CREATE_SUCCESS = 'created'

@api_view(['DELETE',])
#@permission_classes((IsAuthenticated, ))
def api_delete_person_view(request, pk):

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
def api_update_person_view(request,pk):

	try:
		info_user = Personal.objects.get(pk=pk)
		print (info_user.image_file)
	except Personal.DoesNotExist:
		return Response(status=status.HTTP_404_NOT_FOUND)

	if request.method == 'PUT':
		serializer = PersonalUpdateSerializer(info_user, data=request.data, partial=True)
		data = {}
		if serializer.is_valid():
			serializer.save()
			data['response'] = UPDATE_SUCCESS
			data['pk'] = info_user.pk
			data['first_name']=info_user.first_name
			data['last_name'] = info_user.last_name
			data['blood_gp'] = info_user.blood_gp
			return Response(data=data)
		return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)


@api_view(['POST'])
def api_create_personal_view(request):

	if request.method == 'POST':
		print("inside create method!!!!!")
		data = request.data
		serializerboard = PersonalCreateSerializer(data=data)

		data = {}
		if serializerboard.is_valid():
			info = serializerboard.save()
			data['response'] = CREATE_SUCCESS
			data['pk'] = info.pk
			data['first_name'] = info.first_name
			data['last_name'] = info.last_name
			data['blood_gp'] = info.blood_gp
			data['gender']   = info.gender
			data['contact_number'] = info.contact_number
			data['email']  = info.email
			data['group_number'] = info.group_number
			return Response(data=data)
		return Response(serializerboard.errors, status=status.HTTP_400_BAD_REQUEST)

class  PersonalListView(ListAPIView):
	queryset = Personal.objects.all()
	serializer_class = PersonalSerializer
	pagination_class = PageNumberPagination
	filter_backends = (SearchFilter, OrderingFilter)
	search_fields = ('gender', 'blood_gp')
