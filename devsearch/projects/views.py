from django.http import HttpRequest
from django.shortcuts import render
from .models import Project


def projects(request):
    projects_list = Project.objects.all()
    page = 'projects'
    context = {'page': page, 'number': 10, "projects": projects_list}
    return render(request, 'projects/project.html', context)


def singleProject(request, pk):
    project = Project.objects.get(id=pk)
    tags = project.tags.all()
    context = {'project': project, "tags": tags}
    return render(request, 'projects/single-project.html', context)


def createProject(request):
    context = {}
    return render(request, 'projects/project-form.html', context)
