from typing import TYPE_CHECKING, Dict, Any, Union
import pandas as pd
from stock_service.forex.models import Order

if TYPE_CHECKING:
    from stock_service.forex.models import Ticker


class ReportMixin:
    def _load_orders(self, order_type: "Order.OrderType") -> "pd.DataFrame":
        """Load database data and load it as a Pandas Dataframe."""
        orders_df = pd.DataFrame(
            self._ticker.orders.all()
            .filter(type=order_type)
            .values_list("type", "id", "px", "quantity")
        )
        orders_df["value"] = orders_df.apply(lambda row: row[2] * row[3], axis=1)
        orders_df.rename(
            columns={0: "type", 1: "num", 2: "px", 3: "quantity"}, inplace=True
        )

        return orders_df

    def _average(self, df: "pd.DataFrame", column: str) -> float:
        """Return the average by a column."""
        return df[column].mean()

    def _bigger_order(self, df: "pd.DataFrame") -> Dict[str, Any]:
        """Return the bigger order."""
        row = dict(df.loc[(df["value"].idxmax())])
        row.pop("type")

        return row

    def _lower_order(self, df: "pd.DataFrame") -> Dict[str, Any]:
        """Return the bigger order."""
        row = dict(df.loc[(df["value"].idxmin())])
        row.pop("type")

        return row

    def _total_px(self, df: "pd.DataFrame"):
        """Return the px total."""
        return df["px"].sum()

    def _total_qty(self, df: "pd.DataFrame"):
        """Return the px total."""
        return df["quantity"].sum()

    def _total_value(self, df: "pd.DataFrame"):
        """Return the px total."""
        return df["quantity"].sum()

    def statistics(self) -> Dict[str, Any]:
        """Generate report."""
        if isinstance(self, BidReport):
            key = "bids"
        else:
            key = "asks"

        result = {
            key: {
                "average_value": self._average(df=self._df, column="value"),
                "greater_value": self._bigger_order(df=self._df),
                "lesser_value": self._lower_order(df=self._df),
                "total_qty": self._total_qty(df=self._df),
                "total_px": self._total_px(df=self._df),
            }
        }

        return result


class BidReport(ReportMixin):
    def __init__(self, ticker: "Ticker") -> None:
        """Class constructor."""  # noqa: D401
        self._ticker = ticker
        self._df = self._load_orders(order_type=Order.OrderType.BID)


class AskReport(ReportMixin):
    def __init__(self, ticker: "Ticker") -> None:
        """Class constructor."""  # noqa: D401
        self._ticker = ticker
        self._df = self._load_orders(order_type=Order.OrderType.ASK)


def factory_report(
    report_type: "Order.OrderType", ticker: "Ticker"
) -> Union["BidReport", "AskReport"]:
    """Return a report instance based on the report type."""
    map_class = {Order.OrderType.BID: BidReport, Order.OrderType.ASK: AskReport}

    class_ = map_class.get(report_type)

    return class_(ticker)


class ReportGenerator:
    _ticker: "Ticker"
    _report_type: "Order.OrderType"

    def __init__(self, ticker: "Ticker", type: "Order.OrderType") -> None:
        """Class constructor."""  # noqa: D401
        self._ticker = ticker
        self._report_type = type

    @property
    def ticker(self) -> "Ticker":
        return self._ticker

    def statistics_report(self) -> Dict[str, Any]:
        """Create the report for Bid orders."""
        report = factory_report(self._report_type, self.ticker)
        data = report.statistics()

        return data

    def total_report(self) -> Dict[str, Any]:
        """Create the total report"""
        report = factory_report(self._report_type, self.ticker)
        data = report.statistics()

        return data
