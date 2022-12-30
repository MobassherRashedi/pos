from django.urls import path
from .views import AssetHomeView,get_asset_data,post_asset_data,\
    AssetDetailsView,AssetUpdateView,AssetDeleteView


urlpatterns = [
    path('', AssetHomeView.as_view(), name='asset.home'),
    path('details/<int:pk>', AssetDetailsView.as_view(), name='asset.details'),
    path('update/<int:pk>', AssetUpdateView.as_view(), name='asset.update'),
    path('delete/<int:pk>', AssetDeleteView.as_view(), name='asset.delete'),
    path('get/data/', get_asset_data, name='asset.get_data'),
    path('post/data/', post_asset_data, name='asset.post_data'),
]

