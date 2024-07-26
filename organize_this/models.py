from django.db import models

# Shelving Unit
class Shelving_Unit(models.Model):
    name = models.CharField(max_length=100, unique=True)
    room = models.CharField(max_length=100)
    notes = models.TextField()
