from django.urls import path
from .views import AccountsHomeView 

urlpatterns = [
    path('', AccountsHomeView.as_view(), name='accounts.home'),
]
