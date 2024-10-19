from django.shortcuts import render, redirect
from django.urls import reverse_lazy
from django.views.generic import ListView, DetailView, CreateView, UpdateView, DeleteView
from products.models import Product
from .forms import CreateProductForm
from django.urls import reverse


class ProductListView(ListView):
    model = Product
    template_name = 'product_list.html'
    

    
class DetailProductView(DetailView):
    template_name = 'product_detail.html'
    model = Product



class CreateProductView(CreateView):
    model = Product
    form_class = CreateProductForm
    template_name = 'product_create.html'
    success_url = reverse_lazy("product_list")
            


class UpdateProductView(UpdateView):
    template_name = 'product_update.html'
    model = Product
    form_class = CreateProductForm

    def get_success_url(self):
        return reverse_lazy("product_detail", kwargs={ 'pk':self.object.pk })



class DeleteProductView(DeleteView):
    template_name = 'product_delete.html'
    model = Product

    def get_success_url(self):
        return reverse("product_list")
