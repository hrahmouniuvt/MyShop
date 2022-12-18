from django import forms
from .models import OrderForm


class OrderForm(forms.ModelForm):
    class Meta:
        models = OrderFormfields = ['first_name', 'last_name', 'phone', 'email', 'address_line_1','address_line_2', 'country', 'state', 'city', 'order_note']
