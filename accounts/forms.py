from django import forms
from django.contrib.auth.models import User
from django.contrib.auth.forms import UserCreationForm, UserChangeForm

from .models import Profile


class CreateUserForm(UserCreationForm):
    email = forms.EmailField(required=True)

    class Meta:
        model = User
        fields = [
            'username',
            'email',
            'first_name',
            'password1',
            'password2',
        ]

    def save(self, commit=True):
        user = super(CreateUserForm, self).save(commit=False)
        user.save(self.cleaned_data['email'])
        user.save(self.cleaned_data['first_name'])

        if commit:
            user.save()

        return user


class EditUserForm(UserChangeForm):
    class Meta:
        model = User
        fields = [
            'username',
            'first_name',
            'last_name',
            'email',
            'is_staff',
            'password'
        ]

        exclude = []  # Fields your don't want in your form


class EditProfile(forms.ModelForm):  # forms.Form?
    class Meta:
        model = Profile
        fields = [
            'age',
            'user_avatar'
        ]
