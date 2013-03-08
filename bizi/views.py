# Create your views here.
from django.views.generic.list_detail import object_list
from bizi.models import Station
from bizi import loader

LOADER = loader.StationsLoader()

def list_stations(request):
    LOADER.get_bizi_stations() # update stations
    return object_list(request, queryset=Station.objects.all())
    
