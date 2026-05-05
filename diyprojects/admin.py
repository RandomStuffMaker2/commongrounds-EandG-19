from django.contrib import admin
from .models import ProjectCategory, Project, Favorite
# Register your models here.

class FavoriteInLine(admin.StackedInline):
    model = Favorite
    can_delete = True

class ProjectCategoryAdmin(admin.ModelAdmin):
    model = ProjectCategory

class ProjectAdmin(admin.ModelAdmin):
    model = Project
    inlines = [FavoriteInLine]

admin.site.register(ProjectCategory, ProjectCategoryAdmin)
admin.site.register(Project, ProjectAdmin)