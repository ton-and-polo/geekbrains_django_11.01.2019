from django.shortcuts import render, get_object_or_404, redirect
from django.contrib.auth.models import User
from django.contrib.auth.forms import UserChangeForm, UserCreationForm
from django.contrib.auth.decorators import user_passes_test


from accounts.forms import (
    CreateUserForm,
    EditUserForm
)

# Create your views here.


def is_staff(user):
    return user.is_staff


@user_passes_test(is_staff)
def home_view(request):
    users = User.objects.all()

    staff = [user for user in users if user.is_staff]
    non_staff = [user for user in users if not user.is_staff]
    context = {
        'users': users,
        'staff': staff,
        'non_staff': non_staff
    }
    return render(request, 'my_admin/home.html', context)

@user_passes_test(is_staff)
def user_read_view(request, username):
    user = get_object_or_404(User, username=username)
    context = {
        'user': user
    }
    return render(request, 'my_admin/user_read.html', context)


@user_passes_test(is_staff)
def user_update_view(request, username):
    user_update = User.objects.get(username=username)
    if request.method == 'POST':
        form = EditUserForm(request.POST, instance=user_update)
        if form.is_valid():
            form.save()
            return redirect('my_admin:home')
    else:
        form = EditUserForm(instance=user_update)

    context = {
        'form': form
    }
    return render(request, 'my_admin/user_update.html', context)


@user_passes_test(is_staff)
def user_delete_view(request, username):
    user_delete = get_object_or_404(User, username=username)

    if request.method == 'POST':
        user_delete.delete()
        return redirect('my_admin:home')

    context = {
        'user_delete': user_delete
    }

    return render(request, 'my_admin/user_delete.html', context)


@user_passes_test(is_staff)
def user_create_view(request):
    if request.method == 'POST':
        form = UserCreationForm(request.POST)
        if form.is_valid():
            form.save()
            return redirect('my_admin:home')
    else:
        form = UserCreationForm()

    context = {
        'form': form
    }
    return render(request, 'my_admin/user_create.html', context)