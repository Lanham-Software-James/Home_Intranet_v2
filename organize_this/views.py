from unittest import loader
from django.http import HttpResponse
from organize_this.models import Shelf, Shelving_Unit, Tote
from django.http import HttpResponse
from django.template import loader

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

#####################################################################################
#                               function list_totes()                               #
#       This view is called when listing all totes at .../organize_this/totes       #
#####################################################################################
def list_totes(request):
    totes = Tote.objects.raw(''' SELECT 
                                        ott.id, 
                                        ott.name, 
                                        ott.notes, 
                                        ots.name AS "shelf_name" 
                                    FROM 
                                        organize_this_tote ott 
                                    INNER JOIN 
                                        organize_this_shelf ots 
                                    ON 
                                        ott.shelf_id = ots.id''')
                                        
    template = loader.get_template('list_totes.html')
    context = {
        'totes': totes,
    }

    return HttpResponse(template.render(context, request))