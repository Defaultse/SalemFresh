from rest_framework import serializers
from auth_.models import User
from auth_.serializers import UserSerializer
from core.models import *


class CustomerSerializer(UserSerializer):
    class Meta(UserSerializer.Meta):
        model = Customer
        fields = '__all__'


class ShopOwnerSerializer(UserSerializer):
    class Meta(UserSerializer.Meta):
        model = ShopOwner
        fields = '__all__'


class DeliveryGuySerializer(UserSerializer):
    class Meta(UserSerializer.Meta):
        model = DeliveryGuy
        fields = '__all__'


class ShopSerializer(serializers.Serializer):
    name = serializers.CharField
    location = serializers.CharField
    description = serializers.CharField

    def create(self, valideted_data):
        Shop.objects.create(**valideted_data)

    def update(self, instance, validated_data):
        pass


class ProductSerializer(serializers.ModelSerializer):
    shop = ShopSerializer()

    class Meta:
        model = Shop
        fields = '__all__'


class CategorySerializer(serializers.ModelSerializer):
    products = ProductSerializer(many=True)

    class Meta:
        model = Category
        fields = ('id', 'name', 'products')