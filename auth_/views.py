import logging
from django.http import Http404
from rest_framework import status, viewsets
from rest_framework.decorators import api_view
from rest_framework.parsers import FormParser, MultiPartParser, JSONParser
from rest_framework.response import Response
from rest_framework.views import APIView
from rest_framework.authtoken.models import Token
from auth_.permissions import IsCustomer, IsDeliverer, IsManager
from auth_.serializers import *

logger = logging.getLogger(__name__)


class CustomerApi(APIView):
    permission_classes = (IsCustomer,)
    serializer_class = CustomerSerializer

    def get_object(self, pk):
        try:
            return Customer.objects.get(id=pk)
        except Customer.DoesNotExist:
            raise Http404

    def put(self, request, pk):
        customer = self.get_object(pk)
        serializer = self.serializer_class(instance=customer, data=request.data)
        logger.info(f'Customer info modified: {customer}')                           # logging
        if serializer.is_valid():
            serializer.save()
            return Response(serializer.data)
        return Response(serializer.errors)


class DelivererApi(APIView):
    permission_classes = (IsDeliverer,)
    serializer_class = DelivererSerializer

    def get_object(self, pk):
        try:
            return Deliverer.objects.get(id=pk)
        except Deliverer.DoesNotExist:
            raise Http404

    def put(self, request, pk):
        deliverer = self.get_object(pk)
        serializer = self.serializer_class(instance=deliverer, data=request.data)
        if serializer.is_valid():
            serializer.save()
            return Response(serializer.data)
        return Response(serializer.errors)


class ProfileViewSet(viewsets.ModelViewSet):
    queryset = Profile.objects.all()
    serializer_class = ProfileSerializer
    parser_classes = (FormParser, MultiPartParser, JSONParser)


@api_view(['POST'])
def customer_registration(request):
    serializer = CustomerSerializer(data=request.data)
    serializer.is_valid(raise_exception=True)
    serializer.save()
    logger.info(f'Customer registered: {serializer.data}')                         # logging
    return Response(serializer.data, status=status.HTTP_201_CREATED)


@api_view(['POST'])
def deliverer_registration(request):
    serializer = DelivererSerializer(data=request.data)
    serializer.is_valid(raise_exception=True)
    serializer.save()
    logger.info(f'Deliverer registered: {serializer.data}')                         # logging
    return Response(serializer.data, status=status.HTTP_201_CREATED)


@api_view(['POST'])
def manager_registration(request):
    serializer = ManagerSerializer(data=request.data)
    serializer.is_valid(raise_exception=True)
    serializer.save()
    logger.info(f'Manager registered: {serializer.data}')                         # logging
    return Response(serializer.data, status=status.HTTP_201_CREATED)


@api_view(['POST'])
def login(request):
    serializer = AuthTokenSerializer(data=request.data)
    serializer.is_valid(raise_exception=True)
    user = serializer.validated_data.get('user')
    token, created = Token.objects.get_or_create(user=user)
    return Response({'token': token.key})


@api_view(['POST'])
def logout(request):
    request.user.auth_token.delete()
    return Response(status=status.HTTP_200_OK)