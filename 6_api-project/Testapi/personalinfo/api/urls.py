from django.urls import path,include
from personalinfo.api import views
from personalinfo.api.views import(
      api_create_personal_view,
      api_update_person_view,
      api_delete_person_view,
      PersonalListView
)

app_name = 'personalinfo'

urlpatterns = [
   
    path('list', PersonalListView.as_view(), name="list"),
	path('create', api_create_personal_view, name="create"),
	path('update/<pk>', api_update_person_view, name="update"),
	path('delete/<pk>',api_delete_person_view, name ="delete")

]
