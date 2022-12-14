from django.urls import path
from .views import ExpensesHomeView 


urlpatterns = [
    path('', ExpensesHomeView.as_view(), name='expenses.home'),
]

