from django.urls import path
from .views import SalesHomeView,SalesCartProductListView,sales_cart_createView,\
    sales_cart_update_view,sales_cart_delete_view

urlpatterns = [
    path('', SalesHomeView.as_view(), name='sales.home'),
    path('cart/create/ajax/', sales_cart_createView, name='sales.cart.create_ajax'),
    path('cart/product/list/', SalesCartProductListView.as_view(), name='sales.cart.product.list'),
    path('cart/product/update/<int:pk>/', sales_cart_update_view, name='sales.cart.product.update'),
    path('cart/product/delete/<int:pk>/', sales_cart_delete_view, name='sales.cart.product.delete'),
]
