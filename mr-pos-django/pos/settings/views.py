from django.shortcuts import render,HttpResponse
from django.shortcuts import redirect
from django.urls import reverse,reverse_lazy
from django.views.generic import TemplateView,DetailView,CreateView
from django.contrib.auth.mixins import LoginRequiredMixin
from .models import Catagory, SubCatagory, Customer, Supplier, CompanyInfo
from .forms import CustomerForm
from django.http import JsonResponse
from django.template.loader import render_to_string

class CreateCustomerView(LoginRequiredMixin,CreateView):
    model = Customer
    form_class  = CustomerForm
    template_name = "settings\create_customer.html"
    
    def get_success_url(self):
        next_url = self.request.GET.get('next',None) # here method should be GET or POST.
        if next_url:
            return "%s" % (next_url) # you can include some query strings as well
        else :
            return reverse_lazy('dashboard.home') # what url you wish to return


def customer_create(request):
    data = dict()
    if request.method == 'POST':
        form = CustomerForm(request.POST)
        if form.is_valid():
            form = form.save()
            data['form_is_valid'] = True
            data['customer_id'] = form.id
            data['customer_name'] = form.first_name +" "+ form.last_name
        else:
            data['form_is_valid'] = False
    else:
        form = CustomerForm()

    form = CustomerForm()
    context = {'form': form}
    data['html_form'] = render_to_string("settings\partials\create_customer.html",
        context,
        request=request,
    )
    return JsonResponse(data)

class SettingsHomeView(LoginRequiredMixin,TemplateView):
    template_name = "settings/index.html"
    
    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        context["customers"] = Customer.objects.all()
        return context
    

class CustomerDetailsView(LoginRequiredMixin,DetailView):
    template_name = "settings/customer_details.html"
    model = Customer
    context_object_name = 'customer'
    
    def get(self, request, *args, **kwargs):
        response = super().get(request, *args, **kwargs)
        self.object = self.get_object()
        from django.core import serializers
        data = serializers.serialize("json", Customer.objects.filter(pk=self.kwargs['pk']))
        if 'X-Requested-With' in request.headers:
            return HttpResponse(data)
        return response
    
    
    
    
