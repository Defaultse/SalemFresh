from django.urls import path
from rest_framework import routers
from core.views import *

# router = routers.SimpleRouter()
# router.register('shop', ShopViewSet, basename='main')

urlpatterns = [
    path('shops/', ShopApiView.as_view()),
    path('shops/<int:pk>/', ShopApiView.as_view()),

    path('product/', ProductApiView.as_view()),
    path('product/<int:pk>/', ProductApiView.as_view()),

    path('category/<int:pk>/', CategoryApiView.as_view()),

    path('customer/<int:pk>/', CustomerApiView.as_view()),

]

# urlpatterns += router.urls
