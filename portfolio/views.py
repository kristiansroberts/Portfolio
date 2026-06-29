from django.shortcuts import render

from portfolio.models import About, Project

def projects_page(request):
    projects = Project.objects.all()
    return render(request, 'portfolio/projects.html', {'projects': projects})

def about_page(request):
    # only one about instance
    about = About.objects.first()
    return render(request, 'portfolio/about.html', {'about': about})