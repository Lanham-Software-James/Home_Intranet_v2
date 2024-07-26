from http.client import HTTPResponse
from unittest import loader
from django.shortcuts import render
from django.http import HttpResponse

from organize_this.models import Shelving_Unit
from django.http import HttpResponse
from django.template import loader

def shelving_units(request):
    units = Shelving_Unit.objects.order_by('id')
    template = loader.get_template('list_shelving_units.html')
    context = {
        'units': units,
    }

    return HttpResponse(template.render(context, request))