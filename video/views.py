import random

from django.core.urlresolvers import reverse_lazy
from django.http.response import HttpResponse
from django.shortcuts import render
from django.views.generic import DetailView
from django.views.generic.list import ListView

from . import models
# Create your views here.
from django.views.generic.base import View








class AssetDetailView(DetailView):
    model = models.Asset

class AssetListView(ListView):
    model = models.Asset
    paginate_by = 36
    queryset = models.Asset.objects.order_by("?")

class SeriesListView(ListView):
    model = models.Series



