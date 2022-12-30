from django.urls import path
from .views import BankHomeView,homeview,add_bank_view,delete_bank_view,bank_edit_json
    # BankTableExportView,

urlpatterns = [
    # path('', BankHomeView.as_view(), name='bank.home'),
    path('', homeview, name='bank.home'),
    path('add/bank/', add_bank_view, name='bank.add'),
    path('edit/<int:pk>/json/', bank_edit_json, name='bank.edit_json'),
    path('delete/<int:pk>/', delete_bank_view, name='bank.delete'),
    # table report Add suffix to reduce code 
    # path('export/table/?format=csv', BankTableExportView.as_view(), name='bank.export_csv'),
    # path('export/table/?format=pdf', BankTableExportView.as_view(), name='bank.export_pdf'),
    # path('export/table/?format=xlsx', BankTableExportView.as_view(), name='bank.export_xlsx'),
    
]
