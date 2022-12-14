from django.urls import path
from .views import BankHomeView

urlpatterns = [
    path('', BankHomeView.as_view(), name='bank.home'),
]
