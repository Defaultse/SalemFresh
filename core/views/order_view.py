from django.http import Http404
from django.shortcuts import get_object_or_404
from rest_framework import viewsets, status
from rest_framework.decorators import action
from rest_framework.permissions import AllowAny
from rest_framework.response import Response
from rest_framework.views import APIView
import logging
from auth_.permissions import IsCustomer
from core.models import Order, DelivererAndOrder
from core.serializers import OrderSerializer, DelivererAndOrderSerializer

logger = logging.getLogger(__name__)


class OrderViewSet(viewsets.ViewSet):
    queryset = Order.objects.all()
    serializer_class = OrderSerializer

    def retrieve(self, request, pk=None):
        orders = Order.objects.get_customer_order(pk)
        serializer = self.serializer_class(orders)
        return Response(serializer.data)

    # user creating order with products
    def create(self, request):
        serializer = self.serializer_class(data=request.data)
        serializer.is_valid(raise_exception=True)
        serializer.save()
        logger.info(f'Order created: {serializer.data}')                              # logging
        return Response(serializer.data, status=status.HTTP_201_CREATED)

    # user confirmation
    def partial_update(self, request, *args, **kwargs):
        instance = Order.objects.get_customer_order(kwargs.get('pk'))
        serializer = OrderSerializer(instance, data=request.data, partial=True)
        serializer.is_valid(raise_exception=True)
        return Response(serializer.data)

    def get_permissions(self):
        if self.action in ['create', 'retrieve', 'partial_update']:
            self.permission_classes = [IsCustomer, ]
        else:
            self.permission_classes = []
        return super(self.__class__, self).get_permissions()


class DelivererAndOrderViewSet(viewsets.ViewSet):
    def retrieve(self, request, pk=None):
        orders = DelivererAndOrder.objects.get_by_deliverer(pk)
        serializer = DelivererAndOrderSerializer(orders)
        return Response(serializer.data)
