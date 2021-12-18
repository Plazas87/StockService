from django.contrib import admin

from .forms import CustomOrderChangeForm, CustomOrderCreateForm
from .models import Order


class OrderAdmin(admin.ModelAdmin):
    add_form = CustomOrderCreateForm
    form = CustomOrderChangeForm
    model = Order
    ordering = ("type",)
    list_display = ["ticker", "px", "quantity", "type"]

    def get_form(self, request, obj=None, **kwargs):
        """Use special form during Order creation."""
        defaults = {}
        if obj is None:
            defaults["form"] = self.add_form
        defaults.update(kwargs)
        return super().get_form(request, obj, **defaults)


admin.site.register(Order, OrderAdmin)
