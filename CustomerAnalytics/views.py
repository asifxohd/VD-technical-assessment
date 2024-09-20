# views.py
from rest_framework import generics
from rest_framework.views import APIView
from rest_framework.response import Response
from .models import Customer, Order
from .serializers import CustomerSerializer, OrderSerializer

class CustomerListCreateView(generics.ListCreateAPIView):
    queryset = Customer.objects.all()
    serializer_class = CustomerSerializer

class OrderListCreateView(generics.ListCreateAPIView):
    queryset = Order.objects.all()
    serializer_class = OrderSerializer

class TopCustomersView(APIView):
    def get(self, request):
        top_customers = Order.top_customers()
        print(top_customers)
        return Response(top_customers)
