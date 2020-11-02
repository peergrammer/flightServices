from django.shortcuts import render
from  .models import Flight, Reservation, Passenger
from .serializers import FlightSerializer, ReservationSerializer, PassengerSerializer
from rest_framework import viewsets


class FlightViewSet(viewsets.ModelViewSet):
    queryset = Flight.objects.all()
    serializer_class = FlightSerializer

class ReservationViewSet(viewsets.ModelViewSet):
    queryset = Reservation.objects.all()
    serializer_class = ReservationSerializer

class PassengerViewSet(viewsets.ModelViewSet):
    queryset = Passenger.objects.all()
    serializer_class = PassengerSerializer


