from django.urls import path
from .views import PurchasesHomeView 


urlpatterns = [
    path('', PurchasesHomeView.as_view(), name='purchases.home'),
]
