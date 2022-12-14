from django.shortcuts import render
from django.views.generic import TemplateView


class StockHomeView(TemplateView):
    template_name = "stocks/index.html"
