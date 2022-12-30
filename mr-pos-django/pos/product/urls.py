from django.urls import path
from .views import ProductHomeView,ProductDetailsView,BarcodeSearchView


urlpatterns = [
    path('', ProductHomeView.as_view(), name='product.home'),
    path('details/<int:pk>/', ProductDetailsView.as_view(), name='product.details'),
    path('details/<str:barcode>/', BarcodeSearchView.as_view(), name='product.search_by_barcode'),
]
