from django.contrib import admin
from portfolio_projects.models import project

class ProjectAdmin(admin.ModelAdmin):
    pass

admin.site.register(project,ProjectAdmin )