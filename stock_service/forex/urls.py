from django.urls import path

from stock_service.forex.views import BidsView, AsksView, AskBidTotalView

urlpatterns = [
    path("<str:ticker>/bids", BidsView.as_view()),
    path("<str:ticker>/asks", AsksView.as_view()),
    path("<str:ticker>/totals", AskBidTotalView.as_view()),
]
