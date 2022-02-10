from rest_framework import serializers
from locations.models import Location


class LocationSerializer(serializers.HyperlinkedModelSerializer):
    class Meta:
        model = Location
        fields = ['city', 'country']
