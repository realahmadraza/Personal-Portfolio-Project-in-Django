from django.shortcuts import render
from portfolio_projects.models import project

def project_index(request):
    projects = project.objects.all()
    context = {
        'projects' : projects
        }
    return render(request, 'portfolio_projects/project_index.html', context)


def project_detail(request, pk):
    projects = project.objects.get(pk=pk)
    context = {
        'projects' : projects
    }
    return render(request, 'portfolio_projects/project_detail.html', context)