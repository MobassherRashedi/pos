from django.urls import path
from .views import SalesHomeView

urlpatterns = [
    path('', SalesHomeView.as_view(), name='sales.home'),
]
