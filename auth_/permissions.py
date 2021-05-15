from rest_framework.permissions import IsAuthenticated

from utils.constants import CUSTOMER, DELIVERYGUY


class IsCustomer(IsAuthenticated):
    def has_permission(self, request, view):
        return super().has_permission(request, view) and request.user.role == CUSTOMER


class IsDeliverer(IsAuthenticated):
    message = "You are not a Deliverer"

    def has_permission(self, request, view):
        return super().has_permission(request, view) and request.user.role == DELIVERYGUY