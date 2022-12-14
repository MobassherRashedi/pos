from django.shortcuts import render
from django.views.generic import TemplateView


class SalesHomeView(TemplateView):
    template_name = "sales/index.html"
