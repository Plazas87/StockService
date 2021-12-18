from django.contrib import admin

from .forms import CustomOrderChangeForm
from .models import Order


class OrderAdmin(admin.ModelAdmin):
    form = CustomOrderChangeForm
    model = Order
    ordering = ("type",)
    list_display = ["px", "quantity", "type"]


admin.site.register(Order, OrderAdmin)
