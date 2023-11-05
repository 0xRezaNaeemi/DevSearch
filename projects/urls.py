from django.urls import path
from . import views

app_name = 'projects'
urlpatterns = [
    path('', views.projects_view, name='projects'),
    path('project/<str:pk>/', views.project_view, name='project'),
    path('create-project/', views.create_project_view, name='create_project'),
    path('update-project/<str:pk>/', views.update_project_view, name='update_project'),
    path('delete-project/<str:pk>/', views.delete_project_view, name='delete_project'),




]
