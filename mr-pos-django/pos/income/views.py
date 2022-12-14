from django.shortcuts import render
from django.views.generic import TemplateView


class IncomeHomeView(TemplateView):
    template_name = "income/index.html"
