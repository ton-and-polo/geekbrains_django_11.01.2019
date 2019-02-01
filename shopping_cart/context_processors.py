from .models import ShoppingCart

def cart_processor(request):
    if request.user.is_authenticated:
        user_cart = ShoppingCart.objects.filter(user=request.user)
        total_quantity = 0
        for order in user_cart:
            total_quantity += order.quantity
        return {'total_quantity': total_quantity}
    else:
        return {'total_quantity': 0}