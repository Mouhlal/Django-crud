from django.urls import path
from .views import Home
from .views import ProductListView

urlpatterns = [
    path('', Home.as_view(), name='home'),
    path('products/', ProductListView.as_view(), name='products'),
]
