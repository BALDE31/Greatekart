from django.core.exceptions import ObjectDoesNotExist
from carts.models import Cart
from django.shortcuts import redirect, render
from store.models import Product
from .models import Cart, CartItem
from django.http import HttpResponse

# Create your views here.


def _cart_id(request):
    return request.session._get_or_create_session_key()


def add_cart(request, product_id):
    # get the product
    product = Product.objects.get(id=product_id)
    print(product)
    try:
        # get the cart using the cart_id present in the session
        cart = Cart.objects.get(cart_id=_cart_id(request))
    except Cart.DoesNotExist:
        cart = Cart.objects.create(
            cart_id=_cart_id(request)
        )
    cart.save()

    try:
        cart_item = CartItem.objects.get(product=product, cart=cart)
        cart_item.quantity += 1
        cart_item.save()
    except CartItem.DoesNotExist:
        cart_item = CartItem.objects.create(
            product=product,
            quantity=1,
            cart=cart,
        )
        cart_item.save()
    return HttpResponse(cart_item.product.product_name)
    exit()
    return redirect('cart')

def cart(request, total=0, quantity=0, cart_item=None):
    cart = Cart.objects.get(cart_id=_cart_id(request))
    cart_items = CartItem.objects.filter(cart=cart, is_active=True)
    for car_item in cart_items:
        try:
            total = (car_item.product.price * car_item.quantity)
            quantity += cart_item.quantity
        except ObjectDoesNotExist:
            pass

        context = {
            'total': total,
            'quantity': quantity, 
            'cart_items': cart_items
        }


    return render(request, 'cart/cart.html', context)
