# urls.py
from django.urls import path
from .views import CustomerListCreateView, OrderListCreateView, TopCustomersView

urlpatterns = [
    path('customers/', CustomerListCreateView.as_view(), name='customer-list-create'),
    path('orders/', OrderListCreateView.as_view(), name='order-list-create'),
    path('top-customers/', TopCustomersView.as_view(), name='top-customers'),
]
