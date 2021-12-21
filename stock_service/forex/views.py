from typing import Union, Type

from django.http import Http404
from rest_framework.views import APIView, Response

from stock_service.forex.models import Ticker, Order
from stock_service.forex.statistics import ReportGenerator, factory_report


class BidsView(APIView):
    def get(self, request, ticker: str) -> Union[Type[Http404], Response]:
        """Return the bids' report."""
        data = {"data": {}}

        try:
            ticker = Ticker.objects.get(name=ticker)
        except Ticker.DoesNotExist:
            return Response(data=data)

        strategy = factory_report(report_type=Order.OrderType.BID, ticker=ticker)

        reporter = ReportGenerator(strategy)
        report = reporter.stats_report()

        data.update({"data": report})

        return Response(data=data)


class AsksView(APIView):
    def get(self, request, ticker: str) -> Union[Type[Http404], Response]:
        """Return the Asks' report."""
        data = {"data": {}}

        try:
            ticker = Ticker.objects.get(name=ticker)
        except Ticker.DoesNotExist:
            return Response(data=data)

        strategy = factory_report(report_type=Order.OrderType.ASK, ticker=ticker)

        reporter = ReportGenerator(strategy)
        report = reporter.stats_report()

        data.update({"data": report})

        return Response(data=data)


class AskBidTotalView(APIView):
    def get(self, request, ticker: str) -> Union[Type[Http404], Response]:
        """Return the Asks' report."""
        data = {"data": {}}

        result = {ticker: {}}

        try:
            ticker_instance = Ticker.objects.get(name=ticker)
        except Ticker.DoesNotExist:
            return Http404

        bids_strategy = factory_report(
            report_type=Order.OrderType.BID, ticker=ticker_instance
        )
        bids_reporter = ReportGenerator(bids_strategy)

        asks_strategy = factory_report(
            report_type=Order.OrderType.ASK, ticker=ticker_instance
        )
        asks_reporter = ReportGenerator(asks_strategy)

        bids_report = bids_reporter.total_report()
        asks_report = asks_reporter.total_report()

        result[ticker_instance.name].update(bids_report)
        result[ticker_instance.name].update(asks_report)

        data.update({"data": result})

        return Response(data=data)
