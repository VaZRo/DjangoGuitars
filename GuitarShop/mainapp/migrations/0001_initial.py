# Generated by Django 4.2.7 on 2024-01-20 10:59

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Brand',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(max_length=100, unique=True, verbose_name='brand Name')),
                ('description', models.TextField(blank=True, verbose_name='description')),
                ('id_deleted', models.BooleanField(default=False)),
            ],
            options={
                'verbose_name': 'brand',
                'verbose_name_plural': 'brands',
            },
        ),
        migrations.CreateModel(
            name='Category',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(max_length=100, unique=True, verbose_name='name')),
                ('description', models.TextField(blank=True, verbose_name='description')),
                ('id_deleted', models.BooleanField(default=False)),
            ],
            options={
                'verbose_name': 'category',
                'verbose_name_plural': 'categories',
            },
        ),
        migrations.CreateModel(
            name='Color',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(max_length=64, unique=True, verbose_name='color Name')),
                ('is_deleted', models.BooleanField(default=False)),
            ],
            options={
                'verbose_name': 'color',
                'verbose_name_plural': 'colors',
            },
        ),
        migrations.CreateModel(
            name='Type',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(max_length=64, unique=True, verbose_name='type name')),
                ('description', models.TextField(blank=True, verbose_name='description')),
                ('id_deleted', models.BooleanField(default=False)),
            ],
            options={
                'verbose_name': 'type',
                'verbose_name_plural': 'types',
            },
        ),
        migrations.CreateModel(
            name='Product',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(max_length=100, verbose_name='name')),
                ('image', models.ImageField(blank=True, upload_to='product_images/', verbose_name='image')),
                ('short_description', models.TextField(blank=True, max_length=100, verbose_name='short description')),
                ('description', models.TextField(blank=True, verbose_name='description')),
                ('price', models.DecimalField(decimal_places=2, default=0, max_digits=8, verbose_name='price')),
                ('quantity', models.PositiveIntegerField(default=0, verbose_name='quantity in stock')),
                ('created_at', models.DateTimeField(auto_now_add=True)),
                ('updated_at', models.DateTimeField(auto_now=True)),
                ('is_deleted', models.BooleanField(default=False)),
                ('brand', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='mainapp.brand', verbose_name='brand')),
                ('category', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='mainapp.category', verbose_name='category')),
                ('color', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='mainapp.color', verbose_name='color')),
                ('type', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='mainapp.type', verbose_name='type')),
            ],
            options={
                'verbose_name': 'product',
                'verbose_name_plural': 'products',
            },
        ),
    ]
