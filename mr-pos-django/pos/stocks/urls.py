from django.urls import path
from .views import StockHomeView,stock_search_view

urlpatterns = [
    path('', StockHomeView.as_view(), name='stocks.home'),
    path('product/search/', stock_search_view, name='stocks.search'),
]
