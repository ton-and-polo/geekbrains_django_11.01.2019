from django.urls import path


from .views import (
    register_view,
    profile_view,
    profile_update_view
)

app_name = 'accounts'
urlpatterns = [
    path('register/', register_view, name='register'),
    path('profile/', profile_view, name='profile'),
    path('update-profile/', profile_update_view, name='profile_update')
]