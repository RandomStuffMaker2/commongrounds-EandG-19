from django.shortcuts import render
from django.http import HttpResponse
from .models import ProjectCategory, Project, Favorite
from accounts.models import Profile

# Create your views here.
def project_list(request):
    projects = Project.objects.all()
    currentUser = request.user
    if currentUser.is_authenticated:
        currentProfile = currentUser.profile
        createdProjects = currentProfile.projects.all()
        favProjects = Project.objects.filter(profile__profile=currentProfile)
        ctx = {
            'projects': projects, 'createdProjects': createdProjects, 'favProjects': favProjects
        }
    else:
        ctx = {
            'projects': projects
        }
    return render(request, "diyprojects/list.html", ctx)

def project_detail(request, id):
    ctx = {
        'project': Project.objects.get(pk=id)
    }
    return render(request, "diyprojects/project.html", ctx)