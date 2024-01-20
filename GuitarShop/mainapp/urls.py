from django.urls import path, include
from mainapp.views import products, product, get_products

app_name = 'products'

urlpatterns = [
    path('', products, name='index'),
    path('product/<int:pk>/', product, name='product'),
    path('get-products/', get_products, name='get_products'),
    path('auth/', include('authapp.urls', namespace='auth')),
]