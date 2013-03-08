from django.db import models

class Station(models.Model):
    id = models.CharField(max_length=255, primary_key=True)
    address = models.CharField(max_length=1024)
    slots_available = models.IntegerField(default=0)
    bikes_available = models.IntegerField(default=0)


