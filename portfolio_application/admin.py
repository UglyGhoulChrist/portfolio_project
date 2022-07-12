from django.contrib import admin
from .models import Skill, Project


@admin.register(Skill)
class SkillAdmin(admin.ModelAdmin):
    list_display = ['title', 'description', 'picture']


@admin.register(Project)
class ProjectAdmin(admin.ModelAdmin):
    list_display = ['title', 'description', 'picture', 'link_project']
