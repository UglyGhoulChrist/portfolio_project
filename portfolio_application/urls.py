from django.urls import path
from portfolio_application.views import index, about, projects, contacts

urlpatterns = [
    path('', index, name='hello'),
    path('about/', about, name='about'),
    path('projects/', projects, name='projects'),
    path('contacts/', contacts, name='contacts'),
]
