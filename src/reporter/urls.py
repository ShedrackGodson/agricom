from django.urls import path
from .views import HomeView, wards_datasets


urlpatterns = [
    path('home/', HomeView.as_view(), name="home"),
    path('wards_datasets/', wards_datasets, name="wards_datasets"),
]
