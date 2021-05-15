from django.contrib.auth import authenticate
from django.utils.translation import ugettext_lazy as _
from rest_framework import serializers
from auth_.models import *


class AuthTokenSerializer(serializers.Serializer):
    email = serializers.CharField(
        label=_("Email"),
        write_only=True
    )
    password = serializers.CharField(
        label=_("Password"),
        style={'input_type': 'password'},
        trim_whitespace=False,
        write_only=True
    )
    token = serializers.CharField(
        label=_("Token"),
        read_only=True
    )

    def validate(self, attrs):
        email = attrs.get('email')
        password = attrs.get('password')

        if email and password:
            user = authenticate(request=self.context.get('request'),
                                email=email, password=password)
            if not user:
                msg = _('Unable to log in with provided credentials.')
                raise serializers.ValidationError(msg, code='authorization')
        else:
            msg = _('Must include "email" and "password".')
            raise serializers.ValidationError(msg, code='authorization')
        attrs['user'] = user
        return attrs


class CustomUserSerializer(serializers.Serializer):
    email = serializers.EmailField()
    first_name = serializers.CharField()
    last_name = serializers.CharField()
    role = models.SmallIntegerField()
    password = serializers.CharField(write_only=True)

    def create(self, validated_data):
        pass

    def update(self, instance, validated_data):
        pass


class ManagerSerializer(CustomUserSerializer):
    def create(self, validated_data):
        validated_data['role'] = SHOP_MANAGER
        validated_data['is_superuser'] = True
        if validated_data['email'] is None:
            raise TypeError('Users must have an email address.')
        manager = CustomUser(**validated_data)
        manager.set_password(validated_data['password'])
        manager.save()
        return manager

    def update(self, instance, validated_data):
        instance.email = validated_data.get('email', instance.email)
        instance.first_name = validated_data.get('first_name', instance.first_name)
        instance.last_name = validated_data.get('last_name', instance.last_name)
        instance.role = validated_data.get('role', instance.role)
        # instance.password = validated_data.get('password', instance.password)
        instance.save()
        return instance


class CustomerSerializer(CustomUserSerializer):
    location = serializers.CharField
    address = serializers.CharField

    def create(self, validated_data):
        validated_data['role'] = CUSTOMER
        if validated_data['email'] is None:
            raise TypeError('Users must have an email address.')
        customer = Customer(**validated_data)
        customer.set_password(validated_data['password'])
        customer.save()
        return customer

    def update(self, instance, validated_data):
        instance.email = validated_data.get('email', instance.email)
        instance.first_name = validated_data.get('first_name', instance.first_name)
        instance.last_name = validated_data.get('last_name', instance.last_name)
        instance.location = validated_data.get('location', instance.location)
        instance.address = validated_data.get('address', instance.address)
        instance.role = validated_data.get('role', instance.role)
        # instance.password = validated_data.get('password', instance.password)
        instance.save()
        return instance


class DelivererSerializer(CustomUserSerializer):
    completed_orders_count = serializers.IntegerField(allow_null=True, required=False)

    def create(self, validated_data):
        validated_data['role'] = DELIVERYGUY
        if validated_data['email'] is None:
            raise TypeError('Users must have an email address.')
        customer = Deliverer(**validated_data)
        customer.set_password(validated_data['password'])
        customer.save()
        return customer

    def update(self, instance, validated_data):
        instance.email = validated_data.get('email', instance.email)
        instance.first_name = validated_data.get('first_name', instance.first_name)
        instance.last_name = validated_data.get('last_name', instance.last_name)
        instance.completed_orders_count = validated_data.get('completed_orders_count', instance.completed_orders_count)
        instance.role = validated_data.get('role', instance.role)
        # instance.password = validated_data.get('password', instance.password)
        instance.save()
        return instance


class ProfileSerializer(serializers.ModelSerializer):
    class Meta:
        model = Profile
        fields = ('user', 'avatar',)