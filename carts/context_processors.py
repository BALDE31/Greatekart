from .models import CartItem, Cart
from .views import _cart_id


def counter(request):
    cart_count = 0
    if 'admin' in request.path:
        return []
    else:
        try:
            cart = Cart.objects.filter(cart_id=_cart_id(request))
            cart_items = CartItem.objects.filter(cart=cart[:1])
            for car_item in cart_items:
                cart_count += car_item.quantity

        except Cart.DoesNotExist:
            cart_count = 0
    return dict(cart_count=cart_count)
