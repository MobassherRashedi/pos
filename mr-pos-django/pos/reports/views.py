from django.shortcuts import render
from django.views.generic import TemplateView


class ReportsHomeView(TemplateView):
    template_name = "reports/index.html"
