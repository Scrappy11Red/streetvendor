from django.shortcuts import render
from products.models import Product
from django.views.generic import ListView

class HomeView(ListView):
    model = Product
    template_name = 'home.html'


def about_page(request):
    return render(request, 'about.html')


def contact_page(request):
    return render(request, 'contact.html')
