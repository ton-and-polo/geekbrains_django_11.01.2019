from django.shortcuts import render, HttpResponseRedirect, get_object_or_404
from django.contrib.auth.decorators import login_required

from .models import ShoppingCart
from products.models import Product

@login_required
def cart(request):
    user_cart = ShoppingCart.objects.filter(user=request.user)

    price = 0
    amount = 0
    for order in user_cart:
        price += order.product.price * order.quantity
        amount += order.quantity

    context = {
        'title': 'cart',
        'user_cart': user_cart,
        'price': price,
        'amount': amount
    }
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
    elif user_cart.quantity == 0:
        user_cart.delete()

    return HttpResponseRedirect(request.META.get('HTTP_REFERER'))