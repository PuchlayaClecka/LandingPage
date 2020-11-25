from django.urls import path
from .views import product_view, products_view

urlpatterns = [
    path('', products_view, name='products'),
    path('products/<slug:uuid>/', product_view, name='product_detail')
]
