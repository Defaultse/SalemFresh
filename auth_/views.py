from django.http import Http404
from rest_framework import status, viewsets
from rest_framework.decorators import api_view
from rest_framework.parsers import FormParser, MultiPartParser, JSONParser
from rest_framework.permissions import AllowAny
from rest_framework.response import Response
from rest_framework.views import APIView
from rest_framework.authtoken.models import Token
from auth_.permissions import IsCustomer
from auth_.serializers import *


class CustomerApi(APIView):
    permission_classes = (IsCustomer,)
    serializer_class = CustomerSerializer

    def get_object(self, pk):
        try:
            return Customer.objects.get(id=pk)
        except Customer.DoesNotExist:
            raise Http404

    def get(self, request):
        customers = Customer.objects.all()
        serializer = self.serializer_class(customers, many=True)
        return Response({"customers": serializer.data})

    def put(self, request, pk):
        customer = self.get_object(pk)
        serializer = self.serializer_class(instance=customer, data=request.data)
        if serializer.is_valid():
            serializer.save()
            return Response(serializer.data)
        return Response(serializer.errors)


class DelivererApi(APIView):
    permission_classes = (AllowAny,)
    serializer_class = DelivererSerializer

    def get_object(self, pk):
        try:
            return Deliverer.objects.get(id=pk)
        except Deliverer.DoesNotExist:
            raise Http404

    def get(self, request):
        deliverer = Deliverer.objects.all()
        serializer = self.serializer_class(deliverer, many=True)
        return Response({"deliverers": serializer.data})

    def put(self, request, pk):
        deliverer = self.get_object(pk)
        serializer = self.serializer_class(instance=deliverer, data=request.data)
        if serializer.is_valid():
            serializer.save()
            return Response(serializer.data)
        return Response(serializer.errors)

    def post(self, request):
        serializer = self.serializer_class(data=request.data)
        serializer.is_valid(raise_exception=True)
        serializer.save()
        return Response(serializer.data, status=status.HTTP_201_CREATED)


class ProfileViewSet(viewsets.ModelViewSet):
    queryset = Profile.objects.all()
    serializer_class = ProfileSerializer
    parser_classes = (FormParser, MultiPartParser, JSONParser)


@api_view(['POST'])
def customer_registration(request):
    serializer = CustomerSerializer(data=request.data)
    serializer.is_valid(raise_exception=True)
    serializer.save()
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