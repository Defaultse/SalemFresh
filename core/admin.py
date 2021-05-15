from django.contrib import admin
from django.contrib.admin.views.main import ChangeList
from core.forms import OrderChangeListForm
from core.models import *

admin.site.register(Category)
admin.site.register(Product)

admin.site.register(Order)
admin.site.register(DelivererAndOrder)

admin.site.register(ShopFeedback)
admin.site.register(ProductFeedback)






# class OrderChangeList(ChangeList):
#     def __init__(self, request, model, list_display,
#                  list_display_links, list_filter, date_hierarchy,
#                  search_fields, list_select_related, list_per_page,
#                  list_max_show_all, list_editable, model_admin):
#
#         super(OrderChangeList, self).__init__(request, model,
#                                               list_display, list_display_links, list_filter,
#                                               date_hierarchy, search_fields, list_select_related,
#                                               list_per_page, list_max_show_all, list_editable,
#                                               model_admin)
#
#         self.list_display = ['action_checkbox', 'name', 'genre']
#         self.list_display_links = ['name']
#         self.list_editable = ['genre']
#
#
# class OrderAdmin(admin.ModelAdmin):
#     def get_changelist(self, request, **kwargs):
#         return OrderChangeList
#
#     def get_changelist_form(self, request, **kwargs):
#         return OrderChangeListForm
