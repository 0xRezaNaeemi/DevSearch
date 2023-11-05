from django.shortcuts import render, HttpResponse
from .models import Project


def projects_view(request):
    projects = Project.objects.all()
    context = {
        'projects': projects
    }
    return render(request, 'projects/projects.html', context)


def project_view(request, pk):
    project = Project.objects.get(id=pk)
    # tags = project.tags.all()
    context = {
        'project': project,
        # 'tags': tags,
    }
    return render(request, 'projects/single-project.html', context)
