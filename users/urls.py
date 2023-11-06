from django.urls import path
from . import views

app_name = 'users'
urlpatterns = [
    path('', views.profiles_view, name='profiles'),
    path('profile/<str:pk>/', views.user_profile_view, name='user_profile'),
]
