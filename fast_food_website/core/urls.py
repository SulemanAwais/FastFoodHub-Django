from django.urls import path
from .views import *

urlpatterns = [
    path('', LandingPageView.as_view(), name='landing_page'),
    path('menu/', MenuPageView.as_view(), name='menu'),
    path('special-deals/', SpecialDealsPageView.as_view(), name='special_deals'),
]
