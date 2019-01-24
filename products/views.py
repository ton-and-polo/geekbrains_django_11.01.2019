from django.shortcuts import render, get_object_or_404

from .models import Product

# Create your views here.

def products_list_view(request):
    products = Product.objects.all()
    context = {
        "products": products
    }
    return render(request, "products/products_list.html", context)

def product_details_view(request ,id):
    product = get_object_or_404(Product, id=id)
    context = {
        "product": product
    }
    return render(request, "products/product_details.html", context)
