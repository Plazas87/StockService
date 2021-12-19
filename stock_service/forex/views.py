from typing import Union, Type

from django.http import Http404
from rest_framework.views import APIView, Response

from stock_service.forex.models import Ticker, Order
from stock_service.forex.statistics import ReportGenerator


class BidsView(APIView):
    def get(self, request, ticker: str) -> Union[Type[Http404], Response]:
        """Return the bids' report."""
        data = {"data": {}}

        try:
            ticker = Ticker.objects.get(ticker_name=ticker)
        except Ticker.DoesNotExist:
            return Http404

        reporter = ReportGenerator(ticker=ticker, type=Order.OrderType.BID)
        report = reporter.statistics_report()

        data.update({"data": report})

        return Response(data=data)


class AsksView(APIView):
    def get(self, request, ticker: str) -> Union[Type[Http404], Response]:
        """Return the Asks' report."""
        data = {"data": {}}

        try:
            ticker = Ticker.objects.get(ticker_name=ticker)
        except Ticker.DoesNotExist:
            return Http404

        reporter = ReportGenerator(ticker=ticker, type=Order.OrderType.ASK)
        report = reporter.statistics_report()

        data.update({"data": report})

        return Response(data=data)


class AskBidView:
    def get(self, request, ticker: str) -> Union[Type[Http404], Response]:
        """Return the Asks' report."""
        data = {"data": {}}

        try:
            ticker = Ticker.objects.get(ticker_name=ticker)
        except Ticker.DoesNotExist:
            return Http404

        reporter = ReportGenerator(ticker=ticker, type=Order.OrderType.ASK)
        report = reporter.statistics_report()

        data.update({"data": report})

        return Response(data=data)
