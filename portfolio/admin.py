from django.contrib import admin

from portfolio.models import Project

@admin.register(Project)
class ProjectAdmin(admin.ModelAdmin):
    list_display = ('title', 'featured', 'sort_order')
    list_editable = ('featured', 'sort_order')
    search_fields = ('title', 'description')
    
