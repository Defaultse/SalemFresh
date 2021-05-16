from django.db.models import F
from django.http import Http404
from django.shortcuts import get_object_or_404
from rest_framework import viewsets, status
from rest_framework.decorators import action
from rest_framework.permissions import AllowAny
from rest_framework.response import Response
from rest_framework.views import APIView
import logging

from auth_.models import Deliverer
from auth_.permissions import IsCustomer, IsDeliverer
from core.models import Order, DelivererAndOrder
from core.serializers import OrderSerializer, DelivererAndOrderSerializer

logger = logging.getLogger(__name__)


class OrderViewSet(viewsets.ViewSet):
    queryset = Order.objects.all()
    serializer_class = OrderSerializer

    def list(self, request):
        customer_id = request.user.customer.id
        queryset = Order.objects.get_customer_orders(customer_id)
        serializer = self.serializer_class(queryset, many=True)
        return Response(serializer.data)

    def retrieve(self, pk=None):
        orders = Order.objects.get_customer_orders(pk)
        serializer = self.serializer_class(orders)
        return Response(serializer.data)

    # user creating order with products
    def create(self, request):
        request.data['customer']=request.user.customer.id
        serializer = self.serializer_class(data=request.data)
        serializer.is_valid(raise_exception=True)
        serializer.save()
        logger.info(f'Order created: {serializer.data}')  # logging
        return Response(serializer.data, status=status.HTTP_201_CREATED)

    # user confirmation
    def partial_update(self, request, *args, **kwargs):
        instance = Order.objects.get(id=kwargs.get('pk'))
        serializer = self.serializer_class(instance, data=request.data, partial=True)
        serializer.is_valid(raise_exception=True)
        serializer.save()
        logger.info(f'Order executed: {serializer.data}')  # logging
        return Response(serializer.data)

    def get_permissions(self):
        if self.action in ['create', 'list', 'retrieve', 'partial_update']:
            self.permission_classes = [IsCustomer, ]
        else:
            self.permission_classes = []
        return super(self.__class__, self).get_permissions()


class DelivererAndOrderViewSet(viewsets.ViewSet):
    def list(self, request):
        deliverer_id = request.user.deliverer.id
        orders = DelivererAndOrder.objects.get_by_deliverer(deliverer_id)
        serializer = OrderSerializer(orders, many=True)
        return Response(serializer.data)

    def retrieve(self, request, pk=None):
        orders = DelivererAndOrder.objects.get_by_deliverer(pk)
        serializer = DelivererAndOrderSerializer(orders)
        return Response(serializer.data)

    def get_permissions(self):
        if self.action in ['list', 'retrieve',]:
            self.permission_classes = [IsDeliverer, ]
        else:
            self.permission_classes = []
        return super(self.__class__, self).get_permissions()
