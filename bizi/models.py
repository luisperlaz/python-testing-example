from django.db import models

class Bizi(models.Model):
    id = models.CharField(max_length=1024, primary_key=True)
    title = models.CharField(max_length=1024)
    anclajesdisponibles_i = models.IntegerField(default=0)
    bicisdisponibles_i = models.IntegerField(default=0)


