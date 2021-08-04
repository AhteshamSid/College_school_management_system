from django.shortcuts import render, redirect
from django.contrib.auth.models import User
from .models import UserProfile
from .forms import ProfileForm


def profile(request, pk):
    profile = UserProfile.objects.get(id=pk)
    context = {
        'profile': profile
    }
    return render(request, 'account/profile.html', context)


def update_profile(request, pk):
    profile = UserProfile.objects.get(id=pk)
    forms = ProfileForm(instance=profile)
    if request.method == 'POST':
        forms = ProfileForm(request.POST, request.FILES, instance=profile)
        if forms.is_valid():
            forms.save()
        return redirect('home')
    context = {
        'forms': forms
    }
    return render(request, 'account/update-profile.html', context)
