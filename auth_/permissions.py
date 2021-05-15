from rest_framework.permissions import IsAuthenticated

from utils.constants import CUSTOMER, DELIVERYGUY, SHOP_MANAGER


class IsCustomer(IsAuthenticated):
    def has_permission(self, request, view):
        return super().has_permission(request, view) and request.user.role == CUSTOMER


class IsDeliverer(IsAuthenticated):
    message = "You are not a Deliverer"

    def has_permission(self, request, view):
        return super().has_permission(request, view) and request.user.role == DELIVERYGUY


class IsManager(IsAuthenticated):
    message = "You are not a Manager"

    def has_permission(self, request, view):
        return super().has_permission(request, view) and request.user.role == SHOP_MANAGER