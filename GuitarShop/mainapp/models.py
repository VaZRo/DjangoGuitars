from django.db import models


class Category(models.Model):
    name = models.CharField(verbose_name='name', max_length=100, unique=True)
    description = models.TextField(verbose_name='description', blank=True)
    id_deleted = models.BooleanField(default=False)

    def __str__(self):
        return self.name

    class Meta:
        verbose_name = 'category'
        verbose_name_plural = 'categories'


class Brand(models.Model):
    name = models.CharField(verbose_name='brand Name', max_length=100, unique=True)
    description = models.TextField(verbose_name='description', blank=True)
    id_deleted = models.BooleanField(default=False)

    def __str__(self):
        return self.name

    class Meta:
        verbose_name = 'brand'
        verbose_name_plural = 'brands'


class Color(models.Model):
    name = models.CharField(verbose_name='color Name', max_length=64, unique=True)
    is_deleted = models.BooleanField(default=False)

    def __str__(self):
        return self.name

    class Meta:
        verbose_name = 'color'
        verbose_name_plural = 'colors'


class Type(models.Model):
    name = models.CharField(verbose_name='type name', max_length=64, unique=True)
    description = models.TextField(verbose_name='description', blank=True)
    id_deleted = models.BooleanField(default=False)

    def __str__(self):
        return self.name

    class Meta:
        verbose_name = 'type'
        verbose_name_plural = 'types'


class Product(models.Model):
    category = models.ForeignKey(Category, on_delete=models.CASCADE, verbose_name='category')
    brand = models.ForeignKey(Brand, on_delete=models.CASCADE, verbose_name='brand')
    color = models.ForeignKey(Color, on_delete=models.CASCADE, verbose_name='color')
    type = models.ForeignKey(Type, on_delete=models.CASCADE, verbose_name='type')

    name = models.CharField(verbose_name='name', max_length=100)
    image = models.ImageField(upload_to='product_images/', blank=True, verbose_name='image')
    short_description = models.TextField(max_length=100, verbose_name='short description', blank=True)
    description = models.TextField(verbose_name='description', blank=True)
    price = models.DecimalField(max_digits=8, decimal_places=2, default=0 ,verbose_name='price')
    quantity = models.PositiveIntegerField(default=0, verbose_name='quantity in stock')

    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)
    is_deleted = models.BooleanField(default=False)

    def __str__(self):
        return self.name

    class Meta:
        verbose_name = 'product'
        verbose_name_plural = 'products'

