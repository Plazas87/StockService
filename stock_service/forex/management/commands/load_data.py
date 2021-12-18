from typing import Dict, Any

from django.conf import settings
import requests
from django.core.management.base import BaseCommand
from ....forex.models import Order


class Command(BaseCommand):
    help = "Load currency data from the Exchange API."

    def add_arguments(self, parser) -> None:
        """Add and argument to the command."""
        parser.add_argument("symbol", nargs="+", type=str)

    def handle(self, *args, **options) -> None:
        """Handle the command."""
        symbol = options["symbol"][0]
        url = settings.EXCHANGE_URL
        data = self._fetch_data(url=url, symbol=symbol)
        self._load_data(data=data)

        self.stdout.write(
            self.style.SUCCESS("%s data has been successfully loaded" % symbol)
        )

    @staticmethod
    def _make_url(url: str, symbol: str) -> str:
        """Build the url."""
        return f"{url}/{symbol}"

    def _fetch_data(self, url: str, symbol: str) -> Dict[str, Any]:
        """Fetch forex data from a URL."""
        r = requests.get(self._make_url(url, symbol))
        dict_data = r.json()

        return dict_data

    def _load_data(self, data: Dict[str, Any]) -> None:
        """Load data into the data base."""
        orders = []
        for data_key in settings.DATA_KEYS:
            for order in data[data_key]:
                order = Order(
                    id=order["num"],
                    px=order["px"],
                    quantity=order["qty"],
                    type=Order.OrderType.BID
                    if data_key == "bids"
                    else Order.OrderType.ASK,
                )

                orders.append(order)

        # Using a Bulk create operation to avoid multiple hits to the database.
        Order.objects.bulk_create(orders)

        # Using stdout
        # https://docs.djangoproject.com/en/4.0/howto/custom-management-commands/#module-django.core.management
        self.stdout.write(self.style.SUCCESS('Successfully loaded "%s"'))
