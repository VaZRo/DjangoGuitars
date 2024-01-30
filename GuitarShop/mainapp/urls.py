from django.urls import path, include
from mainapp.views import products, product, get_products, brand, get_products_by_brand

app_name = 'products'

urlpatterns = [
    path('', products, name='index'),
    path('product/<int:pk>/', product, name='product'),
    path('get-products/', get_products, name='get_products'),
    path('brand/<int:pk>/', brand, name='brand'),
    path('get-products-by-brand/', get_products_by_brand, name='get_products_by_brand'),
]