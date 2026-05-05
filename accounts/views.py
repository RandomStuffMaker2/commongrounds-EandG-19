from django.shortcuts import render, redirect
from django.http import HttpResponse, HttpResponseNotFound
from django.db import transaction
from .models import Profile
from .forms import ProfileForm
from django.contrib.auth.decorators import login_required

# Create your views here.
@login_required
def profileupdate(request, name):
    currentUser = request.user
    currentProfile = currentUser.profile
    if name == currentProfile.displayName:
        form = ProfileForm()
        if request.method == 'POST':
            form = ProfileForm(request.POST, instance = currentProfile)
            if form.is_valid():
                user = form.save(commit=False)
                currentUser.username = user.displayName
                currentUser.save()
                user.save()
                return redirect('localevents:event_list')
    else:
        return HttpResponseNotFound()
    ctx = {
        'profileform': form
    }
    return render(request, "accounts/profile_update.html", ctx)