from django.shortcuts import render, redirect
from django.contrib.auth.forms import UserCreationForm
from django.contrib.auth import (
    login,
    authenticate
)


# Create your views here.

def register_view(request):
    user_form = UserCreationForm()
    if request.method == 'POST':
        user_form = UserCreationForm(request.POST)
        if user_form.is_valid():
            user_form.save()
            # Authenticate new user:
            new_user = authenticate(
                user_name=user_form.cleaned_data['username'],
                password=user_form.cleaned_data['password1'],
            )
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