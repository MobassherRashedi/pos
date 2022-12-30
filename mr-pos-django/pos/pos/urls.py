from django.contrib import admin
from django.urls import path,include

urlpatterns = [
    # path('__debug__/', include('debug_toolbar.urls')),
    path('admin/', admin.site.urls),
    path('', include('dashboard.urls')),
    path('accounts/', include('accounts.urls')),
    path('asset/', include('asset.urls')),
    path('sales/', include('sales.urls')),
    path('purchases/', include('purchases.urls')),
    path('stocks/', include('stocks.urls')),
    path('bank/', include('bank.urls')),
    path('quotation/', include('quotation.urls')),
    path('income/', include('income.urls')),
    path('expenses/', include('expenses.urls')),
    path('damages/', include('damages.urls')),
    path('hrm/', include('hrm.urls')),
    path('sms/', include('sms.urls')),
    path('settings/', include('settings.urls')),
    path('products/', include('product.urls')),
    path('reports/', include('reports.urls')),
]
