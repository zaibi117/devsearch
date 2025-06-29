from django.http import HttpRequest
from django.shortcuts import render

projects_list = [
    {'id':1, 'title':'E-commerce web app', 'description':'A web app for online shopping'},
    {'id':2, 'title':'Blog app', 'description':'A web app for writing and sharing articles'},
    {'id':3, 'title':'Portfolio app', 'description':'A web app for showcasing your projects'},
]

def projects(request):
    page = 'projects'
    context = {'page': page, 'number': 10 , "projects": projects_list}
    return render(request, 'projects/project.html',context)

def singleProject(request, pk):
    for i in projects_list:
        if i['id'] == pk:
            project = i
    context={'project': project}
    return render(request, 'projects/single-project.html',context)