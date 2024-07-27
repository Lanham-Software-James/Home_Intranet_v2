from django.contrib import admin
from .models import Shelf, Shelving_Unit, Tote

# Register your models here.
admin.site.register(Shelving_Unit)
admin.site.register(Shelf)
admin.site.register(Tote)
