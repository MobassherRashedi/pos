from django.shortcuts import render, get_object_or_404
from django.urls import reverse_lazy
from django.http import HttpResponseRedirect 
from django.views.generic import TemplateView
from django.contrib.auth.mixins import LoginRequiredMixin
from django.http import JsonResponse
from .forms import BankForm,BankTransactionForm,BankTransactionTypeForm
from .tables import BankTable,BankTransactionTypeTable,BankTransactionTable
from .models import Bank,BankTransaction,BankTransactionType
from django.template.loader import render_to_string
import django_tables2 as tables
from django_tables2 import RequestConfig

class BankHomeView(LoginRequiredMixin,TemplateView):
    template_name = "bank/index.html"

def homeview(request):
    form  = BankForm()
    queryset = Bank.objects.all()
    table = BankTable(queryset)
    RequestConfig(request).configure(table)
    context = {
        'form' : form,
        'table' : table,
    }
    return render(request, 'bank/index.html', context)


def add_bank_view(request):
    # retrieve the model instance to be edited
    if request.method == "POST":
        form = BankForm(request.POST or None)
        print(form)
        if form.is_valid():
            form.save()   
    else:
        form = BankForm()
    context = {
        'form': form,
    } 
    url = reverse_lazy('bank.home')
    return HttpResponseRedirect(url)


def delete_bank_view(request, pk):
    data = {}
    instance = Bank.objects.get(pk=pk)
    context = {
        'elm_pk':pk,
        'instance': instance,
    }
    data['form_is_valid'] = True
    data['html_form'] = render_to_string("bank/partials/delete_confirm_form.html",
        context,
        request=request
    )
    if request.method == 'POST':
        instance.delete()
        data['redirect'] = reverse_lazy("bank.home")
        data['success'] = True
        
    return JsonResponse(data)


def bank_edit_json(request, pk):
    data ={}
    bank =Bank.objects.get(id=pk)
    if request.method == 'POST':
        form = BankForm(request.POST, instance=bank)
        if form.is_valid():
            form.save()
            data['form_is_valid'] = True
            data['redirect'] = reverse_lazy("bank.home")
            queryset = Bank.objects.all()
            table = BankTable(queryset)
            RequestConfig(request).configure(table)
            context={
                'table': table,
            }
            data['table'] = render_to_string('bank/partials/bank_table.html',
                        context,
                        request=request
                    )
    else:
        form = BankForm(instance=bank)
        data['form_is_valid'] = False
    context = {
        'elm_pk':pk,
        'form': form,
    }
    data['html_form'] = render_to_string("bank/partials/form.html",
        context,
        request=request
    )
    return JsonResponse(data)


# --------------------------------------Table export view----------------------------------- #

# class BankTableExportView(tables.views.TableExportView):
#     table_class = BankTable
