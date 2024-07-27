from django.db import models

class Shelving_Unit(models.Model):
    name = models.CharField(max_length=100, unique=True)
    room = models.CharField(max_length=100)
    notes = models.TextField(blank=True)

class Shelf(models.Model):
    name = models.CharField(max_length=100, unique=True)
    unit = models.ForeignKey(Shelving_Unit, on_delete=models.DO_NOTHING)
    notes = models.TextField(blank=True)

class Tote(models.Model):
    name = models.CharField(max_length=100, unique=True)
    unit = models.ForeignKey(Shelving_Unit, on_delete=models.DO_NOTHING)
    shelf = models.ForeignKey(Shelf, on_delete=models.DO_NOTHING)
    notes = models.TextField(blank=True)

class Item(models.Model):
    name = models.CharField(max_length=100, unique=True)
    shelf = models.ForeignKey(Shelf, on_delete=models.DO_NOTHING, blank=True, null=True)
    tote = models.ForeignKey(Tote, on_delete=models.DO_NOTHING, blank=True, null=True)
    notes = models.TextField(blank=True)