from django.urls import path
from . import views


urlpatterns = [
	path('', views.list_jobs, name='list_jobs'),
	path('api/get_jobs/', views.get_jobs)
] 

