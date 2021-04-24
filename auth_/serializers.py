from rest_framework import serializers
from auth_.models import *


class UserSerializer(serializers.ModelSerializer):
    class Meta:
        model = User
        fields = '__all__'

    # username = CharField
    # first_name = CharField
    # last_name = CharField
    # email = CharField
    # is_staff = BooleanField
    # is_active = BooleanField
    # date_joined = DateTimeField
    # roles = SmallIntegerField
    # bio = TextField
    #
    # def create(self, valideted_data):
    #     User.objects.create(**valideted_data)
    #
    # def update(self, instance, validated_data):
    #     pass