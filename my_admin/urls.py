from django.urls import path
from .views import (
    home_view,
    user_read_view,
    user_create_view,
    user_update_view,
    user_delete_view,
    user_pwd_change_view
)


app_name = 'my_admin'

urlpatterns = [
    # My_patterns
    path('', home_view, name='home'),
    # CRUD:
    path('read_user_<str:username>', user_read_view, name='user-read'),
    path('create_user/', user_create_view, name='user-create'),
    path('update_user_<str:username>', user_update_view, name='user-update'),
    path('delete_user_<str:username>', user_delete_view, name='user-delete'),
    # Change password:
    path('change_pwd_user_<str:username>', user_pwd_change_view, name='user-change-pwd'),
]