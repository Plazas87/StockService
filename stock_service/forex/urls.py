from django.urls import path

from stock_service.forex.views import BidsView, AsksView, AskBidTotalView

urlpatterns = [
    path("general/<str:ticker>/bids", BidsView.as_view()),
    path("general/<str:ticker>/asks", AsksView.as_view()),
    path("general/<str:ticker>/totals", AskBidTotalView.as_view()),
]
