from django.shortcuts import render
from django.views.generic import TemplateView


class SettingsHomeView(TemplateView):
    template_name = "settings/index.html"
