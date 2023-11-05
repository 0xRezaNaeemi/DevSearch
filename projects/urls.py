from django.urls import path
from . import views

app_name = 'projects'
urlpatterns = [
    path('', views.projects, name='projects'),
    path('<str:pk>', views.project, name='project'),


]
