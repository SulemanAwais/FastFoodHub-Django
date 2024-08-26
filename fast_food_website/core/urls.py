from django.urls import path
from . import views

urlpatterns = [
    path('', LandingPageView.as_view(), name='landing_page'),
    path('menu/', MenuPageView.as_view(), name='menu'),
]
