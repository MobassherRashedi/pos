from django.shortcuts import render
from django.views.generic import TemplateView


class PurchasesHomeView(TemplateView):
    template_name = "purchases/index.html"
