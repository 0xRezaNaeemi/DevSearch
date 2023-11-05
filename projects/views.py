from django.shortcuts import render
from .models import Project
from .froms import ProjectForm


def projects_view(request):
    projects = Project.objects.all()
    context = {
        'projects': projects
    }
    return render(request, 'projects/projects.html', context)


def project_view(request, uuid):
    project = Project.objects.get(id=uuid)
    # tags = project.tags.all()
    context = {
        'project': project,
        # 'tags': tags,
    }
    return render(request, 'projects/single-project.html', context)


def create_project_view(request):
    form = ProjectForm()
    context = {
        'form': form,
    }
    return render(request, 'projects/projects-form.html', context)
