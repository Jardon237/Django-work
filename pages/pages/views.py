from django.shortcuts import render

# Create your views here.
class HomepageView(TemplateView):
    template_name = "home.html"
