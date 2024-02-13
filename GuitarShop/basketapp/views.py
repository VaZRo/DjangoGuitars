from django.contrib.auth.decorators import login_required
from django.shortcuts import render, get_object_or_404
from django.http import HttpResponseRedirect, JsonResponse
from django.template.loader import render_to_string
from django.urls import reverse

from mainapp.models import Product
from .models import Basket
from mainapp.views import get_data
from authapp.views import login


@login_required
def basket(request):
    if request.user.is_authenticated:
        user_basket = Basket.objects.filter(user=request.user)
        context = get_data(basket=user_basket)
        return render(request, 'basket/basket.html', context)
    return HttpResponseRedirect(request.META.get('HTTP_REFERER'))


@login_required
def basket_add(request, pk):
    if request.headers.get('x-requested-with') == 'XMLHttpRequest':

        product = get_object_or_404(Product, pk=pk)
        user_basket = Basket.objects.filter(user=request.user, product=product).first()

        if not user_basket:
            user_basket = Basket(user=request.user, product=product)

        user_basket.quantity += 1
        user_basket.save()

        basket_items = Basket.objects.filter(user=request.user)

        context = {
            'basket': basket_items,
        }

        result = render_to_string('includes/inc_basket_list.html', context)
        return JsonResponse({'result': result})


@login_required
def basket_remove(request, pk):
    if request.headers.get('x-requested-with') == 'XMLHttpRequest':
        basket_item = get_object_or_404(Basket, pk=pk)
        basket_item.delete()

        basket_items = Basket.objects.filter(user=request.user)

        context = {
            'basket': basket_items,
        }
        result = render_to_string('includes/inc_basket_list.html', context)
        return JsonResponse({'result': result})


@login_required
def basket_edit(request, pk, quantity):
    if request.headers.get('x-requested-with') == 'XMLHttpRequest':
        basket_item = Basket.objects.get(pk=pk)
        if quantity > 0:
            basket_item.quantity = quantity
            basket_item.save()
        else:
            basket_item.delete()

        basket_items = Basket.objects.filter(user=request.user)

        context = {
            'basket': basket_items,
        }

        result = render_to_string('includes/inc_basket_list.html', context)
        return JsonResponse({'result': result})
