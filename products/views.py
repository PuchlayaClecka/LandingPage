from django.shortcuts import render

# Create your views here.
from products.models import Product


def product_view(request, uuid: str):
    product = Product.objects.get(uuid=uuid)
    context = {
        'product': product
    }
    return render(request, "product.html", context)


def products_view(request, *args, **kwargs):
    products = Product.objects.all()
    context = {
        'products': products
    }
    return render(request, "products.html", context)
