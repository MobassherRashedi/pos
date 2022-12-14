from django.shortcuts import render
from django.views.generic import TemplateView


class SmsHomeView(TemplateView):
    template_name = "sms/index.html"
