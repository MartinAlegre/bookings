from django.shortcuts import render
from rest_framework import viewsets
from flights.models import Bookings, ClassFlight
from flights.serializers import Bookingserializer, ClassFlightSerializer

class BookingViewSet(viewsets.ModelViewSet):

    serializer_class = Bookingserializer

    def get_queryset(self):
        qs = Bookings.objects.all()
        return qs

class ClassFlightViewSet(viewsets.ModelViewSet):

    serializer_class = ClassFlightSerializer

    def get_queryset(self):
        qs = ClassFlight.objects.all()
        return qs

