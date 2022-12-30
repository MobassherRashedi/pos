from django.shortcuts import render,HttpResponse
from django.views.generic import TemplateView,DetailView
from django.contrib.auth.mixins import LoginRequiredMixin
from .models import ProductImages, ProductUnitType, Product


class ProductHomeView(LoginRequiredMixin,TemplateView):
    template_name = "product/index.html"

class ProductDetailsView(LoginRequiredMixin,DetailView):
    template_name = "product/product_details.html"
    model = Product
    context_object_name = 'product'
    
    def get(self, request, *args, **kwargs):
        response = super().get(request, *args, **kwargs)
        self.object = self.get_object()
        from django.core import serializers
        data = serializers.serialize("json", Product.objects.filter(pk=self.kwargs['pk']))
        if 'X-Requested-With' in request.headers:
            return HttpResponse(data)
        return response
    
class BarcodeSearchView(TemplateView):
    template_name = "sales/index.html"
    
    def get(self, request, *args, **kwargs):
        response = super().get(request, *args, **kwargs)
        from django.core import serializers
        data = serializers.serialize("json", Product.objects.filter(product_code__icontains=self.kwargs['barcode']))
        if 'X-Requested-With' in request.headers:
            return HttpResponse(data)
        return response