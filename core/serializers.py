from rest_framework import serializers
from core.models import *


class ProductSerializer(serializers.ModelSerializer):
    class Meta:
        model = Product
        fields = '__all__'


class CategorySerializer(serializers.ModelSerializer):
    class Meta:
        model = Category
        fields = '__all__'


class CategoryProductsSerializer(serializers.ModelSerializer):
    name = serializers.CharField(read_only=True)
    products = ProductSerializer(many=True)

    class Meta:
        model = Category
        fields = ('id', 'name', 'products')


class ShopFeedbackSerializer(serializers.ModelSerializer):
    class Meta:
        model = ShopFeedback
        fields = '__all__'


class ProductFeedbackSerializer(serializers.ModelSerializer):
    class Meta:
        model = ProductFeedback
        fields = '__all__'


class OrderSerializer(serializers.ModelSerializer):
    class Meta:
        model = Order
        fields = '__all__'


class DelivererAndOrderSerializer(serializers.ModelSerializer):
    order = OrderSerializer(read_only=True)

    class Meta:
        model = DelivererAndOrder
        fields = '__all__'


class ProductFullSerializer(ProductSerializer):
    category = CategorySerializer()

    class Meta(ProductSerializer.Meta):
        fields = ProductSerializer.Meta.fields + 'category'
