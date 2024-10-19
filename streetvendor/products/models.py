from django.db import models
from users.models import User

# Create your models here.

class Category(models.Model):
    name = models.CharField(max_length=25, verbose_name="products")

    def __str__(self):
        return self.name
    
    class Meta:
        verbose_name = "Category"
        verbose_name_plural = "Categories"


class Product(models.Model):
    name = models.CharField(max_length=50)
    description = models.CharField(max_length=250)
    price = models.FloatField()
    category = models.ManyToManyField(Category, verbose_name=("category"))
    stock_quantity = models.FloatField()
    image_url = models.ImageField(upload_to="media", blank=True)
    created_at = models.DateTimeField(auto_now=True)
    author = models.ForeignKey(User, on_delete=models.CASCADE, default="1")

    def __str__(self):
        return self.name
    