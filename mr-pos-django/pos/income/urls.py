from django.urls import path
from .views import IncomeHomeView 


urlpatterns = [
    path('', IncomeHomeView.as_view(), name='income.home'),
]
