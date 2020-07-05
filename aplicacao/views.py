from django.shortcuts import render
from rest_framework import viewsets
from .models import Usuario, Reserva
from .serializers import UsuarioSerializer, ReservaSerializer


class UsuarioViewSet(viewsets.ModelViewSet):
    queryset = Usuario.objects.all()
    serializer_class = UsuarioSerializer


class ReservaViewSet(viewsets.ModelViewSet):
    queryset = Reserva.objects.all()
    serializer_class = ReservaSerializer


