from django.shortcuts import render

# Create your views here.

def carts(requests):
    carts = None
    context= {
        carts: carts,
    }

    return render(requests, 'cart/cart.html', context)
