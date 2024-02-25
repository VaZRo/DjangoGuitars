from django import forms
from .models import Card, Order


class CardForm(forms.ModelForm):
    class Meta:
        model = Card
        fields = ['number', 'owner_name', 'cvv', 'validity']


class OrderForm(forms.ModelForm):
    class Meta:
        model = Order
        fields = ['address']