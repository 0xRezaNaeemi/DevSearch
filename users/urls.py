from django.urls import path
from . import views

app_name = 'users'
urlpatterns = [
    path('', views.profiles_view, name='profiles'),
]
