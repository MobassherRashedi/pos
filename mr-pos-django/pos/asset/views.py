from django.shortcuts import render,HttpResponse
from django.views.generic import TemplateView,FormView,DetailView,UpdateView,DeleteView
from django.contrib.auth.mixins import LoginRequiredMixin
from django.urls import reverse_lazy,reverse
from django.http import JsonResponse
from django.template.loader import render_to_string
from django.http import HttpResponseRedirect
from django.core import serializers

from .forms import AssetForm
from .models import Asset

def is_ajax(request):
    return request.META.get('HTTP_X_REQUESTED_WITH') == 'XMLHttpRequest'

class AssetHomeView(LoginRequiredMixin,TemplateView,FormView):
    form_class = AssetForm
    template_name = "asset/index.html"
    success_url = '/'

class AssetDetailsView(LoginRequiredMixin,DetailView):
    model = Asset
    
    def get(self, request, *args,**kwargs):
        response = super().get(request, *args, **kwargs)
        if request.method == 'GET' and request.is_ajax():
            result_list = list(Asset.objects.filter(id=kwargs.get('id'))\
                .values('date', 
                        'name',
                        'amount',
                        'note',
                        'id',
                       ))
            return JsonResponse(result_list, safe=False)
        return response


class AssetUpdateView(LoginRequiredMixin,UpdateView):
    model = Asset
    
    def get(self, request, *args,**kwargs):
        response = super().get(request, *args, **kwargs)
        if request.method == 'GET' and request.is_ajax():
            result_list = list(Asset.objects.filter(id=kwargs.get('id'))\
                .values('date', 
                        'name',
                        'amount',
                        'note',
                        'id',
                       ))
            return JsonResponse(result_list, safe=False)
        return response


class AssetDeleteView(LoginRequiredMixin,UpdateView):
    model = Asset
    
    def get(self, request, *args,**kwargs):
        response = super().get(request, *args, **kwargs)
        if request.method == 'GET' and request.is_ajax():
            result_list = list(Asset.objects.filter(id=kwargs.get('pk'))\
                .values('date', 
                        'name',
                        'amount',
                        'note',
                        'id',
                       ))
            return JsonResponse(result_list, safe=False)
        return response




def get_asset_data(request):
    if is_ajax(request=request) and request.method == "GET":
        result_list = list(Asset.objects.all()\
                .values('date', 
                        'name',
                        'amount',
                        'note',
                        'id',
                       ))
        return JsonResponse(result_list, safe=False)
    return JsonResponse({'message':'Wrong validation'})

# def get_asset_data(request):
#     if is_ajax(request=request) and request.method == "GET":
#         assets= Asset.objects.all()
#         assetserial = serializers.serialize('json', assets)
#         return JsonResponse(assetserial, safe=False)
#     return JsonResponse({'message':'Wrong validation'})


def post_asset_data(request):
    data = dict()
    if request.method == 'POST' and is_ajax(request):
        form = AssetForm(request.POST)
        if form.is_valid():
            form = form.save()
            data['form_is_valid'] = form.id
            data['sucessfull'] = True
        else:
            data['form_is_valid'] = False
            data['sucessfull'] = False
    else:
        data['message'] = 'Wrong method.Bad request...'
    return JsonResponse(data)
