from django.urls import path
from . import views

app_name = 'projects'
urlpatterns = [
    path('', views.projects_view, name='projects'),
    path('<str:pk>', views.project_view, name='project'),


]
