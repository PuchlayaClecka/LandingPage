from django.contrib import admin

from .models import Product, Age
# Register your models here.

admin.site.register(Age)
admin.site.register(Product)
