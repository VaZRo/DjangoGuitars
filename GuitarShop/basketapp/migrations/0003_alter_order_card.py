# Generated by Django 4.2.5 on 2024-02-25 12:10

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('basketapp', '0002_alter_order_card'),
    ]

    operations = [
        migrations.AlterField(
            model_name='order',
            name='card',
            field=models.ForeignKey(blank=True, editable=False, null=True, on_delete=django.db.models.deletion.CASCADE, to='basketapp.card', verbose_name='Карта'),
        ),
    ]
