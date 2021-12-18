import uuid

from django.db import models


class Order(models.Model):
    class OrderType(models.TextChoices):
        BID = "BD", "Bid"
        ASK = "AK", "Ask"

    id = models.PositiveBigIntegerField(primary_key=True, unique=True)
    quantity = models.FloatField(blank=False, null=False)
    px = models.FloatField(blank=False, null=False)
    type = models.CharField(max_length=2, choices=OrderType.choices)
    ticker = models.ForeignKey("Ticker", on_delete=models.CASCADE)

    def __str__(self) -> str:
        """Nice string representation of the object."""
        return f"Order: {self.id} - Type: {self.type} - px: {self.px} - qty: {self.quantity}"


class Ticker(models.Model):
    id = models.UUIDField(primary_key=True, unique=True, default=uuid.uuid4)
    ticker_name = models.CharField(max_length=40, blank=False)

    def __str__(self) -> str:
        """Nice string representation of the object."""
        return f"{self.ticker_name}"
