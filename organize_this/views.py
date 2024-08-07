from unittest import loader
from django.http import HttpResponse
from organize_this.models import Shelf, Shelving_Unit, Tote
from django.http import HttpResponse
from django.template import loader


#####################################################################################################
#                                   function list_shelving_units()                                  #
#       This view is called when listing all shelving units at .../organize_this/shelving_units     #
#####################################################################################################
def list_shelving_units(request):
    units = Shelving_Unit.objects.order_by('id')
    template = loader.get_template('list_shelving_units.html')
    context = {
        'units': units,
    }

    return HttpResponse(template.render(context, request))


#########################################################################################
#                                   function list_shelves()                             #
#       This view is called when listing all shelves at .../organize_this/shelves       #
#########################################################################################
def list_shelves(request):
    shelves = Shelf.objects.raw(''' SELECT 
                                        ots.id, 
                                        ots.name, 
                                        ots.notes, 
                                        otsu.name AS "unit_name" 
                                    FROM 
                                        organize_this_shelf ots 
                                    INNER JOIN 
                                        organize_this_shelving_unit otsu 
                                    ON 
                                        ots.unit_id = otsu.id''')

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


#####################################################################################
#                               function list_items()                               #
#       This view is called when listing all items at .../organize_this/       #
#####################################################################################
def list_items(request):
    items = Tote.objects.raw(''' 
                                SELECT 
                                    oti.id, 
                                    oti.name, 
                                    oti.notes, 
                                    ott.name AS "tote_name",
                                    ots.name AS "shelf_name",
                                    otsu.name AS "unit_name" 
                                FROM 
                                    organize_this_item oti 
                                LEFT JOIN 
                                    organize_this_tote ott 
                                    ON 
                                        oti.tote_id = ott.id
                                LEFT JOIN
                                    organize_this_shelf ots
                                    ON
                                        (oti.shelf_id = ots.id)
                                        OR
                                        (ott.shelf_id = ots.id)
                                LEFT JOIN
                                    organize_this_shelving_unit otsu
                                    ON
                                        (ots.unit_id = otsu.id)
                                        OR
                                        (ott.shelf_id = ots.id AND ots.unit_id = otsu.id)

                            ''')
                                        
    template = loader.get_template('list_items.html')
    context = {
        'items': items,
    }

    return HttpResponse(template.render(context, request))