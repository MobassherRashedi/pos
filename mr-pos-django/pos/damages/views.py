from django.shortcuts import render
from django.views.generic import TemplateView


class DamagesHomeView(TemplateView):
    template_name = "damages/index.html"
