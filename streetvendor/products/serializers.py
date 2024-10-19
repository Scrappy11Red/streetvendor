from rest_framework import serializers
from .models import Product
from .forms import CreateProductForm

class ProductSerializer(serializers.ModelSerializer):
    class Meta:
        model = Product
        form = CreateProductForm()
        fields = ['name', 'description', 'price', 'category', 'stock_quantity', 'image_url', 'created_at']

