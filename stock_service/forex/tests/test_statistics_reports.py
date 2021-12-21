from django.test import TestCase

from stock_service.forex.models import Ticker, Order
from stock_service.forex.statistics import BidReport, AskReport
from stock_service.forex.tests.conftest import generate_fake_orders


class StatisticsReportTestCases(TestCase):
    def setUp(self) -> None:
        """Common configurations for tests."""
        # Create some fake orders to populate de DB.
        self.ticker = Ticker.objects.create(name="BTC-USD")
        generate_fake_orders(self.ticker)

        self.bids_reporter = BidReport(ticker=self.ticker)
        self.asks_reporter = AskReport(ticker=self.ticker)

    def tearDown(self) -> None:
        """Clean the Database."""
        Ticker.objects.all().delete()
        Order.objects.all().delete()

    def test_bids_stats_report(self):
        """Test bids statistics report."""
        # Arrange
        expected_report = {
            "bids": {
                "average_value": 28.5,
                "greater_value": {"px": 9.0, "quantity": 9.0, "num": 9, "value": 81.0},
                "lesser_value": {"px": 0.0, "quantity": 0.0, "num": 0, "value": 0.0},
                "total_qty": 45.0,
                "total_px": 45.0,
            }
        }

        # Act
        result = self.bids_reporter.stats_report()

        # Asserts
        self.assertEqual(result, expected_report)

    def test_asks_stats_report(self):
        """Test asks statistics report."""
        # Arrange
        expected_report = {
            "asks": {
                "average_value": 218.5,
                "greater_value": {
                    "px": 19.0,
                    "quantity": 19.0,
                    "num": 19,
                    "value": 361.0,
                },
                "lesser_value": {
                    "px": 10.0,
                    "quantity": 10.0,
                    "num": 10,
                    "value": 100.0,
                },
                "total_qty": 145.0,
                "total_px": 145.0,
            }
        }

        # Act
        result = self.asks_reporter.stats_report()

        # Asserts
        self.assertEqual(result, expected_report)
