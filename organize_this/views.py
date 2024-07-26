from http.client import HTTPResponse
from unittest import loader
from django.shortcuts import render
from django.http import HttpResponse

from organize_this.models import Shelf, Shelving_Unit
from django.http import HttpResponse
from django.template import loader
from pprint import pprint

def shelving_units(request):
    units = Shelving_Unit.objects.order_by('id')
    template = loader.get_template('list_shelving_units.html')
    context = {
        'units': units,
    }

    return HttpResponse(template.render(context, request))

def shelves(request):
    shelves = Shelf.objects.raw(''' SELECT 
                                        ots.id, 
                                        ots.name, 
                                        ots.notes, 
                                        otsu.name AS "unit" 
                                    FROM 
                                        organize_this_shelf ots 
                                    INNER JOIN 
                                        organize_this_shelving_unit otsu 
                                    ON 
                                        ots.shelving_unit_id = otsu.id''')
                                        
    template = loader.get_template('list_shelves.html')
    context = {
        'shelves': shelves,
    }

    return HttpResponse(template.render(context, request))