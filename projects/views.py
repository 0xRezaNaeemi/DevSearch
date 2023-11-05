from django.shortcuts import render, redirect
from .models import Project
from .froms import ProjectForm


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


def create_project_view(request):
    form = ProjectForm()

    if request.method == "POST":
        form = ProjectForm(request.POST, request.FILES)
        if form.is_valid():
            form.save()
            return redirect('projects:projects')

    context = {
        'form': form,
    }
    return render(request, 'projects/projects-form.html', context)


def update_project_view(request, pk):

    project = Project.objects.get(id=pk)
    form = ProjectForm(instance=project)

    if request.method == "POST":
        form = ProjectForm(request.POST, request.FILES, instance=project)
        if form.is_valid():
            form.save()
            return redirect('projects:projects')

    context = {
        'form': form,
    }
    return render(request, 'projects/projects-form.html', context)


def delete_project_view(request, pk):
    project = Project.objects.get(id=pk)
    form = ProjectForm(instance=project)
    if request.method == "POST":
        project.delete()
        return redirect('projects:projects')
    context = {
        'object': project
    }
    return render(request, 'projects/delete-template.html', context)
