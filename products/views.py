from django.shortcuts import render, get_object_or_404

from .models import Product

# Create your views here.

def products_list_view(request):
    products = Product.objects.all()
    context = {
        "products": products
    }
    return render(request, "products/products_list.html", context)
