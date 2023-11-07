from django.contrib.auth import authenticate, login, logout
from django.contrib import messages
from django.shortcuts import render, redirect
from django.contrib.auth.models import User
from .models import Profile


def login_view(request):

    if request.user.is_authenticated:
        return redirect('users:profiles')

    if request.method == 'POST':
        username = request.POST['username']
        password = request.POST['password']

        try:
            user = User.objects.get(username=username)
        except:
            messages.error(request, 'Username does not exist')

        user = authenticate(request, username=username, password=password)

        if user is not None:
            login(request, user)
            return redirect('users:profiles')
        else:
            messages.error(request, 'Username or Password is incorrect')

    return render(request, 'users/login_register.html')


def logout_view(request):
    logout(request)
    messages.error(request, 'User was logged out!')
    return redirect('users:login')


def profiles_view(request):
    profiles = Profile.objects.all()
    context = {
        'profiles': profiles
    }
    return render(request, 'users/profiles.html', context)


def user_profile_view(request, pk):
    profile = Profile.objects.get(id=pk)
    top_skills = profile.skill_set.exclude(description__exact="")
    other_skills = profile.skill_set.filter(description="")

    context = {
        'profile': profile,
        'top_skills': top_skills,
        'other_skills': other_skills
    }
    return render(request, 'users/user-profile.html', context)
