from django.shortcuts import render
from django.views.generic import TemplateView

class Index(TemplateView):
    template_name: str = "index.html"
    

