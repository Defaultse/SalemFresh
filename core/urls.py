from django.urls import path, include
from rest_framework import routers
from core.views.feedbacks_view import *
from core.views.products_view import *
from core.views.order_view import *

router = routers.SimpleRouter()
router.register('products', ProductViewSet, basename='products')
router.register('categories', CategoryViewSet, basename='categories')
router.register('orders', OrderViewSet, basename='orders')
router.register('deliverer-tasks', DelivererAndOrderViewSet, basename='set-order-deliverer')

urlpatterns = [
    path('category-products/<int:pk>/', CategoryProductsApi.as_view()),

    path('shopfeedbacks/', ShopFeedbackViewSet.as_view({'get': 'list'})),
    path('shopfeedbacks/create/', ShopFeedbackViewSet.as_view({'post': 'create'})),

    path('productfeedbacks/<int:pk>/', ProductFeedbackViewSet.as_view({'get': 'retrieve'})),
    path('productfeedbacks/create/', ProductFeedbackViewSet.as_view({'post': 'create'})),

    path("", include(router.urls)),
]

urlpatterns += router.urls
