from django.contrib import admin
from .models import Category, Brand, Color, Type, Product

admin.site.register(Category)
admin.site.register(Brand)
admin.site.register(Color)
admin.site.register(Type)
admin.site.register(Product)
