from django.contrib import admin
from .models import Basket, Order, Card, OrderDetails


class OrderDetailsInline(admin.TabularInline):  # или admin.StackedInline в зависимости от ваших предпочтений
    model = OrderDetails
    extra = 0
    readonly_fields = ['user', 'product', 'quantity', 'product_cost']
    can_delete = False
    max_num = 0


class OrderAdmin(admin.ModelAdmin):
    readonly_fields = ['card', 'address', 'user']
    inlines = [OrderDetailsInline]


admin.site.register(Card)
admin.site.register(Basket)
admin.site.register(Order, OrderAdmin)
admin.site.register(OrderDetails)
