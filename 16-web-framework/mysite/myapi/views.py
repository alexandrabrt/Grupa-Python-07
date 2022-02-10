from rest_framework import viewsets
from locations.models import Location
from myapi.serializers import LocationSerializer


class LocationsViewSet(viewsets.ModelViewSet):
    queryset = Location.objects.all().order_by('city')
    serializer_class = LocationSerializer
