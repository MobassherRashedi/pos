from django.shortcuts import render,HttpResponse,get_object_or_404
from django.http import HttpResponseRedirect
from django.urls import reverse_lazy,reverse
from django.views.generic import TemplateView,ListView,DetailView,CreateView
from django.views.generic.detail import SingleObjectMixin
from django.contrib.auth.mixins import LoginRequiredMixin
from .forms import SalesForm,SalesCartForm,SalesCartAmountForm
from settings.forms import CustomerForm
from .models import SalesCart, SalesCartAmount, Sales
from product.models import Product
from django.http import JsonResponse
from django.template.loader import render_to_string
from settings.models import Customer
from django.db.models import F
from django.db import models

class BarcodeSearchView(DetailView):
    model = Product
    context_object_name = 'product'
    template_name = "sales/index.html"
    # slug_field = ''
    def get(self, request, *args, **kwargs):
        response = super().get(request, *args, **kwargs)
        self.object = self.get_object()
        from django.core import serializers
        data = serializers.serialize("json", Product.objects.filter(pk=self.kwargs['pk']))
        if 'X-Requested-With' in request.headers:
            return HttpResponse(data)
        return response

class SalesHomeView(LoginRequiredMixin,TemplateView):
    template_name = "sales/index.html"
    
    def get_context_data(self, **kwargs):
        context = super(SalesHomeView, self).get_context_data(**kwargs)
        customer_form = CustomerForm(self.request.GET or None, prefix="customer")
        sales_form = SalesForm(self.request.GET or None, prefix="sales",initial={'purchased_by': self.request.user})
        sales_cart_form = SalesCartForm(self.request.GET or None, prefix="sales_cart")
        sales_cart_amount_form = SalesCartAmountForm(self.request.GET or None, prefix="sales_cart_amount")
        context['sales_form'] = sales_form
        context['sales_cart_form'] = sales_cart_form
        context['sales_cart_amount_form'] = sales_cart_amount_form
        context['customer_form'] = customer_form
        context['user'] = self.request.user
        SaleCarts = SalesCart.objects.all()
        context['SaleCarts'] = SaleCarts
        return context
    

    
class SalesCartProductListView(TemplateView):
    template_name = "sales/index.html"
    
    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        return context

def sales_cart_createView(request):
    data = dict()
    if request.method == 'POST':
        p = request.POST
        user =  Customer.objects.filter(id=p.get('customer_id'))[0]
        product = Product.objects.filter(id=p.get('product_id'))[0]
        quantity = p.get('quantity')
        total = p.get('total')
        SalesCart.objects.create(user=user, product=product,quantity=quantity,total_amount=total)
        data['sucessfull'] = 'true'
        ss =list(SalesCart.objects.filter(user=user).filter(active=True).values())
        # values('id','product__name','product__catagory__name',\
        # 'quantity','product__sales_rate',\
        # 'total_amount'))
        data["SaleCarts"] = ss
        data["redirect"] = reverse_lazy("sales.home")
    else:
        data['sucessfull'] = 'false'
        data['form_is_valid'] = 'false'
    return JsonResponse(data)

#----------------------- update sales cart ----------------#
def save_salescart_form(request, form, template_name):
    data = dict()
    print(request.POST)
    if request.method == 'POST':
        if form.is_valid():
            form.save()
            data['form_is_valid'] = True
            SalesCarts = SalesCart.objects.all()
            context ={
                'SaleCarts': SalesCarts,
            }
            data['html_list'] = render_to_string('sales/partials/sales_table.html',
                 context,
                request=request
            )
        else:
            data['form_is_valid'] = False
        return JsonResponse(data)
    context = {'form': form}
    data['html_form'] = render_to_string(template_name, context, request=request)
    return JsonResponse(data)


def sales_cart_update_view(request, pk):
    salescart = get_object_or_404(SalesCart, pk=pk)
    if request.method == 'POST':
        form = SalesCartForm(request.POST, instance=salescart)
    else:
        form = SalesCartForm(instance=salescart)
    return save_salescart_form(request, form, 'sales/partials/form.html')


def sales_cart_delete_view(request, pk):
    data = {}
    instance = get_object_or_404(SalesCart, pk=pk)
    context = {
        'elm_pk':pk,
        'instance': instance,
    }
    data['form_is_valid'] = True
    data['html_form'] = render_to_string("sales/partials/delete_confirm_form.html",
        context,
        request=request
    )
    if request.method == 'POST':
        instance.delete()
        SalesCarts = SalesCart.objects.all()
        context ={
            'SaleCarts': SalesCarts,
        }
        data['html_list'] = render_to_string('sales/partials/sales_table.html',
                context,
            request=request
        )
        
    return JsonResponse(data)
