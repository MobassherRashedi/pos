from django.urls import path
from .views import HrmHomeView 


urlpatterns = [
    path('', HrmHomeView.as_view(), name='hrm.home'),
]

