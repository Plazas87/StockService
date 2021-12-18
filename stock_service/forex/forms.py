from django.forms import ModelForm

from stock_service.forex.models import Order


class CustomOrderChangeForm(ModelForm):
    class Meta:
        """Meta class"""  # noqa: D401
        model = Order
        fields = ["type", "px", "quantity"]
