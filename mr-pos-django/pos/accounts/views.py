from django.shortcuts import render
from django.views.generic import TemplateView


class AccountsHomeView(TemplateView):
    template_name = "accounts/index.html"
