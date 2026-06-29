from django.contrib import admin

from portfolio.models import Project, About

@admin.register(Project)
class ProjectAdmin(admin.ModelAdmin):
    list_display = ('title', 'featured', 'sort_order')
    list_editable = ('featured', 'sort_order')
    search_fields = ('title', 'description')
    
@admin.register(About)
class AboutAdmin(admin.ModelAdmin):
    list_display = ('resume_link', 'paragraph1', 'paragraph2')
    search_fields = ('paragraph1', 'paragraph2')