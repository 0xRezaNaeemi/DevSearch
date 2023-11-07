from django.urls import path
from . import views

app_name = 'users'
urlpatterns = [
    path('login', views.login_view, name='login'),
    path('logout', views.logout_view, name='logout'),

    path('', views.profiles_view, name='profiles'),
    path('profile/<str:pk>/', views.user_profile_view, name='user_profile'),
]
