from django import forms
from .models import Item


class AddItem(forms.ModelForm):
    class Meta:
        model = Item
        fields = ['title','price','discount_price','description','image','category']
