from django.contrib.auth.mixins import LoginRequiredMixin
from django.shortcuts import render,get_object_or_404
from django.urls import reverse_lazy
from django.views.generic import TemplateView
from django.contrib.auth.mixins import LoginRequiredMixin
from product.models import Product
from django.http import JsonResponse
from django.template.loader import render_to_string
from django.db.models import F
from django.core import serializers

class StockHomeView(LoginRequiredMixin,TemplateView):
    template_name = "stocks/index.html"


def stock_search_view(request):
    data = {'success':'false'}
    query = request.GET.get('option')
    if query=='instock':
        bool_x = True
    else:
        bool_x = False
    ss =list(Product.objects.filter(in_stock=bool_x).values('name','product_code','catagory',\
        'sub_catagory','product_unit',\
        'alert_qty','purchase_rate','sales_rate'))
    # print(ss[0].keys())
    data["products"] = ss
        
    
    # data["products"]=list(Product.objects.filter(in_stock=bool_x).values('name',\
    #      'product_code',catagory=F('catagory__name'),sub_catagory=F('sub_catagory__name'),product_unit__name=F('product_unit__name'),alert_qty=F('alert_qty'),\
    #          purchase_rate=F('purchase_rate'),sales_rate=F('sales_rate')))
    data['success']=True
    return JsonResponse(data)