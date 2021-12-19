from django.urls import path

from stock_service.forex.views import BidsView, AsksView

urlpatterns = [
    path("general/<str:ticker>/bids", BidsView.as_view()),
    path("general/<str:ticker>/asks", AsksView.as_view()),
]
