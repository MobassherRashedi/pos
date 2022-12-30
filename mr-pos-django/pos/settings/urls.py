from django.urls import path
from .views import SettingsHomeView,CustomerDetailsView,CreateCustomerView,customer_create

urlpatterns = [
    path('', SettingsHomeView.as_view(), name='settings.home'),
    path('customer/create/', CreateCustomerView.as_view(), name='settings.customer.create'),
    path('customer/create/ajax/', customer_create, name='settings.customer.create_ajax'),
    path('customer/details/<int:pk>/', CustomerDetailsView.as_view(), name='customer.details'),
]

