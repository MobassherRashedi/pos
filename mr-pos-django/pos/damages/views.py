from django.shortcuts import render
from django.views.generic import TemplateView
from django.contrib.auth.mixins import LoginRequiredMixin

class DamagesHomeView(LoginRequiredMixin,TemplateView):
    template_name = "damages/index.html"
