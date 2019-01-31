from django.urls import path

from .views import (
    cart,
    add_to_cart,
    remove_from_cart
)

app_name = 'shopping_cart'

urlpatterns = [
    path('', cart, name='items-in-cart'),
    path('add/<int:id>/', add_to_cart, name='add_to_cart'),
    path('remove/<int:id>)/', remove_from_cart, name='remove_from_cart'),
]