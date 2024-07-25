from django.shortcuts import render
from rest_framework.generics import ListAPIView, RetrieveAPIView, CreateAPIView
from .models import Drug, Contact, Order
from .serializers import DrugSerializer, ContactSerializer, OrderSerializer


class DrugListApiView(ListAPIView):
    queryset = Drug.objects.all()
    serializer_class = DrugSerializer


class DrugDetailApiView(RetrieveAPIView):
    queryset = Drug.objects.all()
    serializer_class = DrugSerializer


class ContactCreateApiView(CreateAPIView):
    queryset = Contact.objects.all()
    serializer_class = ContactSerializer


class OrderCreateApiView(CreateAPIView):
    queryset = Order.objects.all()
    serializer_class = OrderSerializer

