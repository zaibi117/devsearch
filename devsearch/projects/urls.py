from django.urls import path
from . import views


urlpatterns = [
    path('', views.projects, name='projects'),
    path('project/<uuid:pk>/', views.singleProject, name='project'),
    path('project/create', views.createProject, name='create-project')
]
