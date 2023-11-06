from django.shortcuts import render


def profiles_view(request):
    return render(request, 'users/profiles.html')
