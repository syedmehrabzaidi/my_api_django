from django.urls import include, path 
from rest_framework import routers
from . import views


routers = routers.DefaultRouter()
routers.register(r'student', views.StudentsViewSet)
urlpatterns = [
    path('', include(routers.urls)),
    path('api_auth/', include('rest_framework.urls', namespace='rest_framework')),
]

