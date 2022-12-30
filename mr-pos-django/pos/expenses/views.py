from django.shortcuts import render
from django.views.generic import TemplateView
from django.contrib.auth.mixins import LoginRequiredMixin

class ExpensesHomeView(TemplateView):
    template_name = "expenses/index.html"
