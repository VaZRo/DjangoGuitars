from django.shortcuts import render
from django.http import JsonResponse, HttpResponseBadRequest
from django.urls import reverse
from django.views.decorators.csrf import csrf_protect
from django.views.decorators.http import require_POST
from mainapp.models import Category, Brand, Color, Type, Product
import json


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
                # for pk in brand_pks:
                #     brand_pk = int(pk)
                #     products = products.filter(brand__pk=brand_pk)
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
                })

            return JsonResponse(product_data, safe=False)


    # if request.method == 'POST':
    #     products = Product.objects.all()
    #     filter_data = request.POST.get('filterData', None)
    #
    #     if filter_data:
    #         filter_data = json.loads(filter_data)
    #
    #         brand_pks = filter_data.get('brandPk', [])
    #         type_pks = filter_data.get('typePk', [])
    #         color_pks = filter_data.get('colorPk', [])
    #         category_pks = filter_data.get('categoryPk', [])
    #
    #         if isinstance(brand_pks, list):
    #             for pk in brand_pks:
    #                 brand_pk = int(pk)
    #                 products = products.filter(brand__pk=brand_pk)
    #
    #         if isinstance(type_pks, list):
    #             for pk in type_pks:
    #                 type_pk = int(pk)
    #                 products = products.filter(type__pk=type_pk)
    #
    #         if isinstance(color_pks, list):
    #             for pk in color_pks:
    #                 color_pk = int(pk)
    #                 products = products.filter(color__pk=color_pk)
    #
    #         if isinstance(category_pks, list):
    #             for pk in category_pks:
    #                 category_pk = int(pk)
    #                 products = products.filter(category__pk=category_pk)
    #
    #         product_data = []
    #         for prod in products:
    #             product_data.append({
    #                 "pk": prod.pk,
    #                 "name": prod.name,
    #                 "price": prod.price,
    #                 "image": prod.image.url if prod.image else None,
    #                 "url": reverse('products:product', args=[prod.pk]),
    #             })
    #
    #         # Возвращаем данные в формате JSON
    #         return JsonResponse(product_data, safe=False)
    #     else:
    #         return HttpResponseBadRequest("Invalid filter data")
    # else:
    #     # Если запрос не является POST-запросом, возвращаем ошибку
    #     return HttpResponseBadRequest("Invalid request method")



def index(request):
    prods = Product.objects.all()[:5]
    context = get_data(prods=prods)
    return render(request, 'index.html', context)


def products(request):
    prods = Product.objects.order_by('price')
    context = get_data(prods=prods)
    return render(request, 'products.html', context)


def product(request, pk):
    prod = Product.objects.get(pk=pk)
    context = get_data(prod=prod)

    return render(request, 'product.html', context)
