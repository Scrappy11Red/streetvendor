from django import forms
from .models import Product

class CreateProductForm(forms.ModelForm):
    
    class Meta:
        model = Product
        fields = ['id', 'name', 'description', 'price', 'category', 'stock_quantity', 'image_url']