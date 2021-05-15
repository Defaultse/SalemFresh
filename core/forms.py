from django import forms
from core.models import Order, Product


class OrderChangeListForm(forms.ModelForm):
    # here we only need to define the field we want to be editable
    products = forms.ModelMultipleChoiceField(
        queryset=Product.objects.all(), required=False)