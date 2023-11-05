from django.urls import path
from . import views

app_name = 'projects'
urlpatterns = [
    path('', views.projects_view, name='projects'),
    path('create-project/', views.create_project_view, name='create_project'),
    path('<str:uuid>/', views.project_view, name='project'),



]
