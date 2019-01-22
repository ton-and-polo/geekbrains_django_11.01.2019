from django.urls import path

from .views import (
    products_list_view,
    product_details_view
)

app_name = 'products'
urlpatterns = [
    path('', products_list_view, name='products-list'),
    path('<int:id>/', product_details_view, name='product-details')
]