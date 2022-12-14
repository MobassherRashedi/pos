from django.shortcuts import render
from django.views.generic import TemplateView

class AssetHomeView(TemplateView):
    template_name = "asset/index.html"
