from django.urls import path

from stock_service.forex.views import StatisticView

urlpatterns = [path("general/", StatisticView.as_view())]
