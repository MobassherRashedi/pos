from django.urls import path
from .views import StockHomeView

urlpatterns = [
    path('', StockHomeView.as_view(), name='stocks.home'),
]
