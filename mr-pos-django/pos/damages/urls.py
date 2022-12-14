from django.urls import path
from .views import DamagesHomeView 


urlpatterns = [
    path('', DamagesHomeView.as_view(), name='damages.home'),
]
