from django.urls import path,include
from rest_framework import routers
from . import views

from courses.views import CourseView


router = routers.DefaultRouter()
router.register('',views.CourseView)

urlpatterns = [
    #path('<int:pk>/', StudentViewusingID.as_view()),
    path('', include(router.urls)),
]
