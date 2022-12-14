from django.urls import path
from .views import SmsHomeView 


urlpatterns = [
    path('', SmsHomeView.as_view(), name='sms.home'),
]

