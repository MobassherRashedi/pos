from django.urls import path
from .views import AssetHomeView 


urlpatterns = [
    path('', AssetHomeView.as_view(), name='asset.home'),
]

