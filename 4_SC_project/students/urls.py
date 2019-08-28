from django.urls import path,include
from rest_framework import routers
from . import views

from students.views import StudentsView,StudentViewusingID


router = routers.DefaultRouter()
router.register('',views.StudentsView)

urlpatterns = [
    #path('<int:pk>/', StudentViewusingID.as_view()),
    path('', include(router.urls)),
]
