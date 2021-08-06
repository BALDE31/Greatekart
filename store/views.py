from django.shortcuts import get_object_or_404, render
from store.models import Product
from category.models import Category


def store(request, category_slug=None):
    categories = None
    products = None
    product_count = None

    if category_slug != None:
        categories = get_object_or_404(Category, slug=category_slug)
        products = Product.objects.filter(category=categories, is_available=True)
    else:
        products = Product.objects.all().filter(is_available=True)
        product_count = products.count()

    context = {
        'products': products,
        'product_count': product_count,
    }

    return render(request, 'store/store.html', context)
