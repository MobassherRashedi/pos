from django.urls import path
from .views import SettingsHomeView 


urlpatterns = [
    path('', SettingsHomeView.as_view(), name='settings.home'),
]

