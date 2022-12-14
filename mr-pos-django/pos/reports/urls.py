from django.urls import path
from .views import ReportsHomeView 


urlpatterns = [
    path('', ReportsHomeView.as_view(), name='reports.home'),
]

