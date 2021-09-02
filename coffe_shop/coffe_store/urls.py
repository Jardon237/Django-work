from django.urls import path
from .views import HomepageView, TemplateView

urlpatterns = [
    path('', HomepageView()),
]
