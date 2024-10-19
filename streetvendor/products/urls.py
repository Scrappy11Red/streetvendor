from django.urls import path
from .views import ProductListView, CreateProductView, DetailProductView, UpdateProductView, DeleteProductView 

users_name = "products"

urlpatterns = [
    path('list/', ProductListView.as_view(), name='product_list'),
    path('create/', CreateProductView.as_view(), name='product_create'),
    path('<pk>/', DetailProductView.as_view(), name='product_detail'),
    path('<pk>/update/', UpdateProductView.as_view(), name='product_update'),
    path('<pk>/delete/', DeleteProductView.as_view(), name='product_delete'),
]

