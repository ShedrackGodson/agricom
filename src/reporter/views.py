from django.shortcuts import render
from django.views.generic import TemplateView
from .models import Wards, Incidences
from django.http import HttpResponse
from django.core.serializers import serialize

# Create your views here.
class HomeView(TemplateView):
    template_name = "index.html"


def wards_datasets(request):
    wards = serialize('geojson', Wards.objects.all())
    return HttpResponse(wards, content_type='json')


def incidences_datasets(request):
    incidences = serialize('geojson', Incidences.objects.all())
    return HttpResponse(incidences, content_type='json')