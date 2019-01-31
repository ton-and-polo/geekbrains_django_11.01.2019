from django.shortcuts import render, HttpResponseRedirect, get_object_or_404
from .models import ShoppingCart
from products.models import Product


def cart(request):
    context = {}
    return render(request, 'shopping_cart/cart.html', context)


def add_to_cart(request, id):
    product = get_object_or_404(Product, id=id)

    cart = ShoppingCart.objects.filter(user=request.user, product=product).first()

    if not cart:
        cart = ShoppingCart(user=request.user, product=product)

    cart.quantity += 1
    cart.save()

    return HttpResponseRedirect(request.META.get('HTTP_REFERER'))


def remove_from_cart(request, id):
    product = get_object_or_404(Product, id=id)
    user_cart = ShoppingCart.objects.filter(user=request.user, product=product).first()
    if user_cart.quantity > 0:
        user_cart.quantity -= 1
        user_cart.save()

    return HttpResponseRedirect(request.META.get('HTTP_REFERER'))