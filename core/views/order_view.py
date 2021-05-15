from django.http import Http404
from django.shortcuts import get_object_or_404
from rest_framework import viewsets, status
from rest_framework.decorators import action
from rest_framework.permissions import AllowAny
from rest_framework.response import Response
from rest_framework.views import APIView

from core.models import Order, DelivererAndOrder
from core.serializers import OrderSerializer, DelivererAndOrderSerializer


class OrderViewSet(viewsets.ViewSet):
    def list(self, request):
        queryset = Order.objects.all()
        serializer = OrderSerializer(queryset, many=True)
        return Response(serializer.data)

    def retrieve(self, request, pk=None):
        queryset = Order.objects.all()
        category = get_object_or_404(queryset, pk=pk)
        serializer = OrderSerializer(category)
        return Response(serializer.data)

    # user creating order with products
    def create(self, request):
        serializer = OrderSerializer(data=request.data)
        serializer.is_valid(raise_exception=True)
        serializer.save()
        return Response(serializer.data, status=status.HTTP_201_CREATED)


class DelivererAndOrderViewSet(viewsets.ViewSet):
    @action(detail=True, methods=['put'], name='Set deliverer')
    def put(self, request, pk):
        order = DelivererAndOrder.objects.get_by_order(pk)
        print(request.data)
        serializer = DelivererAndOrderSerializer(instance=order, data=request.data)
        if serializer.is_valid():
            serializer.save()
            return Response(serializer.data)
        return Response(serializer.errors)

