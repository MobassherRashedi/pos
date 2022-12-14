from django.shortcuts import render
from django.views.generic import TemplateView


class ExpensesHomeView(TemplateView):
    template_name = "expenses/index.html"
