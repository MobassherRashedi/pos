from django.shortcuts import render
from django.views.generic import TemplateView


class ProductHomeView(TemplateView):
    template_name = "product/index.html"
