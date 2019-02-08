from django.shortcuts import render, get_object_or_404

from .models import Product, Category
from shopping_cart.models import ShoppingCart

# Create your views here.


def products_list_view(request, category_name):
    categories = Category.objects.all()
    user_cart = ShoppingCart.objects.filter(user=request.user.id)

    if category_name == 'all':
        products = Product.objects.all()
    else:
        category = Category.objects.filter(category_name=category_name)[0]
        products = Product.objects.filter(category=category)



    context = {
        "title": "products",
        "products": products,
        "categories": categories,
        "user_cart": user_cart,
        "all_products": "all"
    }
    return render(request, "products/products_list.html", context)


def product_details_view(request ,id):
    product = get_object_or_404(Product, id=id)
    context = {
        "product": product
    }
    return render(request, "products/product_details.html", context)
