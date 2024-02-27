from django.shortcuts import render
from django.http import JsonResponse, HttpResponseBadRequest
from django.urls import reverse
from django.views.decorators.csrf import csrf_protect
from django.views.decorators.http import require_POST
from mainapp.models import Category, Brand, Color, Type, Product
from basketapp.models import Basket
import json


brand_pk = None

def get_data(**kwargs):
    categories = Category.objects.all()
    brands = Brand.objects.all()
    colors = Color.objects.all()
    types = Type.objects.all()

    context = {
        'categories': categories,
        'brands': brands,
        'colors': colors,
        'types': types,
    }

    context.update(**kwargs)
    return context


def get_basket(user):
    if user.is_authenticated:
        return Basket.objects.filter(user=user)
    return []


@csrf_protect
@require_POST
def get_products(request):
    if request.method == 'POST':
        products = Product.objects.all()
        request_data = json.loads(request.body.decode('utf-8'))
        filter_data = request_data.get('filterData', None)
        # print("Received filter_data:", filter_data)

        if filter_data is not None:
            brand_pks = filter_data.get('brandPk', None)
            type_pks = filter_data.get('typePk', None)
            color_pks = filter_data.get('colorPk', None)
            category_pks = filter_data.get('categoryPk', None)

            if brand_pks is not None:
                products = products.filter(brand__pk__in=brand_pks)

            if type_pks is not None:
                products = products.filter(type__pk__in=type_pks)

            if color_pks is not None:
                products = products.filter(color__pk__in=color_pks)

            if category_pks is not None:
                products = products.filter(category__pk__in=category_pks)

            product_data = []
            for prod in products:
                product_data.append({
                    "pk": prod.pk,
                    "name": prod.name,
                    "price": prod.price,
                    "image": prod.image.url if prod.image else None,
                    "url": reverse('products:product', args=[prod.pk]),
                    "basket_add_url": reverse('basket:add', args=[prod.pk]),
                })

            return JsonResponse(product_data, safe=False)


@csrf_protect
@require_POST
def get_products_by_brand(request):
    if request.method == 'POST':
        brand_ = brand_pk
        products = Product.objects.all().filter(brand=brand_)
        request_data = json.loads(request.body.decode('utf-8'))
        filter_data = request_data.get('filterData', None)

        if filter_data is not None:
            type_pks = filter_data.get('typePk', None)
            color_pks = filter_data.get('colorPk', None)
            category_pks = filter_data.get('categoryPk', None)

            if type_pks is not None:
                products = products.filter(type__pk__in=type_pks)

            if color_pks is not None:
                products = products.filter(color__pk__in=color_pks)

            if category_pks is not None:
                products = products.filter(category__pk__in=category_pks)

            product_data = []
            for prod in products:
                product_data.append({
                    "pk": prod.pk,
                    "name": prod.name,
                    "price": prod.price,
                    "image": prod.image.url if prod.image else None,
                    "url": reverse('products:product', args=[prod.pk]),
                    "basket_add_url": reverse('basket:add', args=[prod.pk]),
                })

            return JsonResponse(product_data, safe=False)


def index(request):
    prods = Product.objects.all()[:5]
    basket = get_basket(request.user)
    brands = Brand.objects.all()[:5]
    context = get_data(prods=prods, basket=basket, brands=brands)
    return render(request, 'index.html', context)


def thanku(request):
    basket = get_basket(request.user)
    context = get_data(basket=basket)
    return render(request, 'thanku.html', context)


def products(request):
    basket = get_basket(request.user)
    context = get_data(basket=basket)
    return render(request, 'products.html', context)


def product(request, pk):
    prod = Product.objects.get(pk=pk)
    basket = get_basket(request.user)
    prods = Product.objects.all()[:5]
    context = get_data(prod=prod, basket=basket, prods=prods)
    return render(request, 'product.html', context)


def brand(request, pk):
    global brand_pk
    brand_pk = pk
    brand_ = Brand.objects.get(pk=pk)
    prods = Product.objects.filter(brand=pk)
    basket = get_basket(request.user)
    context = get_data(prods=prods, basket=basket, brand=brand_)
    return render(request, 'brand.html', context)
