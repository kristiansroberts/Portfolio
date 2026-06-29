from django.shortcuts import render

from portfolio.models import Project

def projects_page(request):
    projects = Project.objects.all()
    return render(request, 'portfolio/projects.html', {'projects': projects})
