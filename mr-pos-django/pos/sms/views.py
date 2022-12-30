from django.shortcuts import render
from django.views.generic import TemplateView
from django.contrib.auth.mixins import LoginRequiredMixin


class SmsHomeView(LoginRequiredMixin,TemplateView):
    template_name = "sms/index.html"
