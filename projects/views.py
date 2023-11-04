from django.shortcuts import render, HttpResponse


PROJECT_LIST_DATA = [
        {'id': "1", 'title': "css", 'description': "css is the best!"},
        {'id': "2", 'title': "html", 'description': "html is the best!"},
        {'id': "3", 'title': "django", 'description': "django is the best!"},
        {'id': "4", 'title': "python", 'description': "python is the best!"},
    ]


def projects(request):

    # data
    msg = "Hello, How are you"
    number = 12
    my_list = (1, 2, 3, 4, 5)

    context = {
        'message': msg,
        'number': number,
        'list': my_list,
        'projects': PROJECT_LIST_DATA
    }
    return render(request, 'projects/projects.html', context)


def project(request, pk):
    project_obj = None
    for i in PROJECT_LIST_DATA:
        if i['id'] == pk:
            project_obj = i

    context = {'project': project_obj}

    return render(request, 'projects/single-project.html', context)
