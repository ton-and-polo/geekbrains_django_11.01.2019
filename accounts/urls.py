from django.urls import path
from django.contrib.auth import views as auth_views

from .views import register_view

app_name = 'accounts'
urlpatterns = [
    path('register/', register_view, name='register'),
    path('login/', auth_views.LoginView.as_view(template_name='registration/login.html'), name='login'),
]