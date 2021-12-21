from typing import TYPE_CHECKING

from stock_service.forex.models import Order

if TYPE_CHECKING:
    from stock_service.forex.models import Ticker


def generate_fake_orders(ticker: "Ticker"):
    """Generate fake orders."""
    orders = []
    for i in range(20):
        order = Order(
            id=i,
            px=i,
            quantity=i,
            type=Order.OrderType.BID if i < 10 else Order.OrderType.ASK,
            ticker=ticker,
        )
        orders.append(order)

    Order.objects.bulk_create(orders)
