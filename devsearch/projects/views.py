from django.shortcuts import render, redirect
from .models import Project
from .forms import ProjectForm


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

    if request.method == 'POST':
        form = ProjectForm(request.POST)
        if form.is_valid():
            form.save()
            return redirect('projects')
    form = ProjectForm()
    context = {'form': form}
    return render(request, 'projects/project_form.html', context)
