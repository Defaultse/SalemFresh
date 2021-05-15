from rest_framework import viewsets, status
from rest_framework.generics import get_object_or_404
from rest_framework.permissions import AllowAny
from rest_framework.response import Response
from auth_.permissions import IsCustomer
from core.models import ShopFeedback, ProductFeedback
from core.serializers import ProductFeedbackSerializer, ShopFeedbackSerializer


class ShopFeedbackViewSet(viewsets.ViewSet):
    def list(self, request):
        queryset = ShopFeedback.objects.all()
        serializer = ShopFeedbackSerializer(queryset, many=True)
        return Response(serializer.data)

    def create(self, request):
        serializer = ShopFeedbackSerializer(data=request.data)
        serializer.is_valid(raise_exception=True)
        serializer.save()
        return Response(serializer.data, status=status.HTTP_201_CREATED)

    def get_permissions(self):
        if self.action in ['list', 'retrieve']:
            self.permission_classes = [AllowAny, ]
        else:
            self.permission_classes = [IsCustomer]
        return super(self.__class__, self).get_permissions()


class ProductFeedbackViewSet(viewsets.ViewSet):
    def list(self, request):
        queryset = ProductFeedback.objects.all()
        serializer = ProductFeedbackSerializer(queryset, many=True)
        return Response(serializer.data)

    def retrieve(self, request, pk=None):
        queryset = ProductFeedback.objects.all()
        feedbacks = get_object_or_404(queryset, pk=pk)
        serializer = ProductFeedbackSerializer(feedbacks)
        return Response(serializer.data)

    def create(self, request):
        serializer = ProductFeedbackSerializer(data=request.data)
        serializer.is_valid(raise_exception=True)
        serializer.save()
        return Response(serializer.data, status=status.HTTP_201_CREATED)

    def get_permissions(self):
        if self.action in ['list', 'retrieve']:
            self.permission_classes = [AllowAny, ]
        else:
            self.permission_classes = [IsCustomer]
        return super(self.__class__, self).get_permissions()