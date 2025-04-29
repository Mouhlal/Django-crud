from django.shortcuts import render
from django.views import View
from .products import products

class Home(View):
    def get(self, request):
        return render(request, 'hello.html')

class ProductListView(View):
    def get(self, request):
        return render(request, 'products.html', {'products': products})

 