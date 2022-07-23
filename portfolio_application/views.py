from django.shortcuts import render
from .models import Project, Skill


def index(request):
    return render(request, 'portfolio_application/hello.html')


def about(request):
    skills = Skill.objects.all()
    return render(request, 'portfolio_application/about.html', {'skills': skills})


def projects(request):
    projects = Project.objects.all()
    return render(request, 'portfolio_application/projects.html', {'projects': projects})


def contacts(request):
    return render(request, 'portfolio_application/contacts.html')
