from rest_framework import serializers
from .models import Bookings, ClassFlight

class Bookingserializer(serializers.ModelSerializer):
    class Meta:
        model = Bookings
        fields = '__all__'

class ClassFlightSerializer(serializers.ModelSerializer):
    class Meta:
        model = ClassFlight
        fields = '__all__'