from django.shortcuts import render
from django.views.generic import TemplateView


class HrmHomeView(TemplateView):
    template_name = "hrm/index.html"
