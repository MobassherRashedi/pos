from django.shortcuts import render
from django.views.generic import TemplateView
from django.contrib.auth.mixins import LoginRequiredMixin


class IncomeHomeView(LoginRequiredMixin,TemplateView):
    template_name = "income/index.html"
