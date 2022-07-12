from django.urls import path
from portfolio_application.views import index, about, my_projects,contacts

urlpatterns = [
    path('', index, name='hello'),
    path('about/', about, name='about'),
    path('my_projects/', my_projects, name='my_projects'),
    path('contacts/', contacts, name='contacts'),
]