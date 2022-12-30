from django.shortcuts import render
from django.views.generic import TemplateView
from django.contrib.auth.mixins import LoginRequiredMixin

class HrmHomeView(LoginRequiredMixin,TemplateView):
    template_name = "hrm/index.html"
