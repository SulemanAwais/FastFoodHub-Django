from django.shortcuts import render

# Create your views here.
from django.shortcuts import render

from django.views.generic import TemplateView


class LandingPageView(TemplateView):
    template_name = 'core/landing_page.html'


class MenuPageView(TemplateView):
    template_name = 'core/menu.html'


class SpecialDealsPageView(TemplateView):
    template_name = 'core/special_deals.html'


class AboutView(TemplateView):
    template_name = 'core/about.html'


class CheckoutPageView(TemplateView):
    template_name = 'core/checkout.html'
