from .models import Custumer, Order
from ordApp.serializer import CustumerSerializer, OrderSerializer
from rest_framework import generics

# Create your views here.


class CustumerListView(generics.ListCreateAPIView):
    queryset = Custumer.objects.all()
    serializer_class = CustumerSerializer


class CustumerDetailView(generics.RetrieveDestroyAPIView):
    queryset = Custumer.objects.all()
    serializer_class = CustumerSerializer


class OrderListView(generics.ListCreateAPIView):
    queryset = Order.objects.all()
    serializer_class = OrderSerializer


class OrderDetailView(generics.RetrieveDestroyAPIView):
    queryset = Order.objects.all()
    serializer_class = OrderSerializer
