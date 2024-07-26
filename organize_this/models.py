from django.db import models

class Shelving_Unit(models.Model):
    name = models.CharField(max_length=100, unique=True)
    room = models.CharField(max_length=100)
    notes = models.TextField()

class Shelf(models.Model):
    name = models.CharField(max_length=100, unique=True)
    shelving_unit_id = models.ForeignKey(Shelving_Unit, on_delete=models.DO_NOTHING)
    notes = models.TextField()
