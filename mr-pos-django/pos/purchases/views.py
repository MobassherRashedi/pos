from django.shortcuts import render
from django.views.generic import TemplateView
from django.contrib.auth.mixins import LoginRequiredMixin


class PurchasesHomeView(LoginRequiredMixin,TemplateView):
    template_name = "purchases/index.html"
