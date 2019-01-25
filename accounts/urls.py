from django.urls import path
from django.contrib.auth import views as auth_views

from .views import (
    register_view,
    profile_view,
)

app_name = 'accounts'
urlpatterns = [
    path('register/', register_view, name='register'),
    path('profile/', profile_view, name='profile'),
    path('login/', auth_views.LoginView.as_view(template_name='registration/login.html'), name='login'),
]