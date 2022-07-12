from django.shortcuts import render

def index(request):
    return render(request, template_name='portfolio_application/hello.html')

def about(request):
    return render(request, template_name='portfolio_application/about.html')

def my_projects(request):
    return render(request, template_name='portfolio_application/my_projects.html')    

def contacts(request):
    return render(request, template_name='portfolio_application/contacts.html')