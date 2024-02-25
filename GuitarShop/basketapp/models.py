from django.db import models
from mainapp.models import Product
from GuitarShop import settings


class Card(models.Model):
    user = models.ForeignKey(
        settings.AUTH_USER_MODEL,
        on_delete=models.CASCADE,
        related_name='card',
    )

    add_datetime = models.DateTimeField(
        verbose_name='время',
        auto_now_add=True,
    )

    number = models.CharField(
        verbose_name='номер',
        max_length=16,
    )

    owner_name = models.CharField(
        verbose_name="имя владельца",
        max_length=100,
    )

    cvv = models.CharField(
        verbose_name='CVV',
        max_length=3,
    )

    validity = models.CharField(
        verbose_name='срок действия',
        max_length=5,
    )

    def __str__(self):
        return self.number

    class Meta:
        verbose_name = 'Карта'
        verbose_name_plural = 'Карты'


class Order(models.Model):
    user = models.ForeignKey(
        settings.AUTH_USER_MODEL,
        on_delete=models.CASCADE,
        related_name='basket'
    )

    add_datetime = models.DateTimeField(
        verbose_name='время',
        auto_now_add=True,
    )

    status = models.CharField(
        verbose_name='статус',
        max_length=100,
    )

    address = models.CharField(
        verbose_name='Адрес',
        max_length=300,
    )

    card = models.ForeignKey(
        Card,
        on_delete=models.CASCADE,
        verbose_name='Карта',
        null=True,
        blank=True,
        editable=False,
    )

    def __str__(self):
        return f"{self.user} - {self.address}"

    class Meta:
        verbose_name = 'Заказ'
        verbose_name_plural = 'Заказы'


class OrderAbstract(models.Model):

    product = models.ForeignKey(
        Product,
        on_delete=models.CASCADE,
    )

    quantity = models.PositiveIntegerField(
        verbose_name='количество',
        default=0,
    )

    add_datetime = models.DateTimeField(
        verbose_name='время',
        auto_now_add=True,
    )

    def __str__(self):
        return f'{self.user.username} - {self.product.name} ({self.quantity} шт.)'

    @property
    def product_cost(self):
        return self.product.price * self.quantity

    class Meta:
        abstract = True


class Basket(OrderAbstract):
    user = models.ForeignKey(
        settings.AUTH_USER_MODEL,
        on_delete=models.CASCADE,
        related_name='baskets'
    )

    @property
    def total_quantity(self):
        _items = Basket.objects.filter(user=self.user)
        _total_quantity = sum(list(map(lambda x: x.quantity, _items)))
        return _total_quantity

    @property
    def total_cost(self):
        _items = Basket.objects.filter(user=self.user)
        _total_cost = sum(list(map(lambda x: x.product_cost, _items)))
        return _total_cost

    class Meta:
        verbose_name = 'Корзина'
        verbose_name_plural = 'Корзины'


class OrderDetails(OrderAbstract):
    user = models.ForeignKey(
        settings.AUTH_USER_MODEL,
        on_delete=models.CASCADE,
        related_name='order_details'
    )

    order = models.ForeignKey(
        Order,
        on_delete=models.CASCADE,
    )

    @property
    def total_quantity(self):
        _items = OrderDetails.objects.filter(user=self.user)
        _total_quantity = sum(item.quantity for item in _items)
        return _total_quantity

    @property
    def total_cost(self):
        _items = OrderDetails.objects.filter(user=self.user)
        _total_cost = sum(item.product_cost for item in _items)
        return _total_cost

    class Meta:
        verbose_name = 'Детали заказа'

