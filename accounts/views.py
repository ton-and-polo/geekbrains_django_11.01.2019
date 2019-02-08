from django.shortcuts import render, redirect, get_object_or_404
from django.contrib.auth.forms import UserCreationForm
from django.contrib.auth import (
    login,
    authenticate
)

from .forms import EditProfile
from .models import Profile

# Create your views here.


def register_view(request):
    user_form = UserCreationForm()
    if request.method == 'POST':
        user_form = UserCreationForm(request.POST)
        if user_form.is_valid():
            user_form.save()
            new_user = user_form.save()
            # Create profile for new user:
            Profile.objects.create(user_id=new_user.id)
            # Login your new user:
            login(request, new_user)
            return redirect('accounts:profile')
        else:
            print(user_form.errors)

    context = {
        'form': user_form
    }
    return render(request, 'accounts/register.html', context)


def profile_view(request):
    context = {}
    return render(request, 'accounts/profile.html', context)


# Fix(doesn't upload user_photo)!
def profile_update_view(request):
    user_id = request.user.id

    instance = get_object_or_404(Profile, user_id=user_id)

    form = EditProfile(instance=instance)
    if request.method == 'POST':
        form = EditProfile(request.POST, request.FILES, instance=instance)
        if form.is_valid():
            form.save()
            return redirect('accounts:profile')

    context = {
        'form': form
    }
    return render(request, 'accounts/update_profile.html', context)