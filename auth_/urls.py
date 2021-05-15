from django.urls import path
from rest_framework import routers
from auth_ import views
from auth_.views import *
from rest_framework_jwt.views import obtain_jwt_token

router = routers.SimpleRouter()
router.register('profile', views.ProfileViewSet, basename='profile')

urlpatterns = [
    path('api-token-auth/', obtain_jwt_token),
    path('login/', views.login),
    path('logout/', views.logout),

    path('customer/', views.CustomerApi.as_view()),
    path('customer/<int:pk>/', views.CustomerApi.as_view()),
    path('customer_registration/', views.customer_registration),

    path('deliverer/', DelivererApi.as_view()),
    path('deliverer/<int:pk>/', views.DelivererApi.as_view()),
    path('deliverer_registration/', views.deliverer_registration),

    path('manager_registration/', views.manager_registration),

]

urlpatterns += router.urls
