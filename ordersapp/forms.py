from django import forms
from ordersapp.models import Order, OrderItem

from .models import Book


class OrderForm(forms.ModelForm):
   class Meta:
       model = Order
       exclude = ('user',)

   def __init__(self, *args, **kwargs):
       print('6666666666666666666666666')
       super().__init__(*args, **kwargs)
       for field_name, field in self.fields.items():
           field.widget.attrs['class'] = 'form-control'
       print('7777777777777777777777777777')


class OrderItemForm(forms.ModelForm):
    price = forms.CharField(label='цена', required=False)

    class Meta:
        model = OrderItem
        exclude = ()

    def __init__(self, *args, **kwargs):
        print('44444444444444444444444444444')
        super().__init__(*args, **kwargs)
        for field_name, field in self.fields.items():
            field.widget.attrs['class'] = 'form-control'

        self.fields['product'].queryset = Book.get_items()
        print('55555555555555555555555555555555')