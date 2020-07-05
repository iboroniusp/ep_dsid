from django.shortcuts import render
from rest_framework import viewsets
from .models import Usuario, ReservaVoo, Reserva
from .serializers import UsuarioSerializer, ReservaSerializer, ReservaVooSerializer


class UsuarioViewSet(viewsets.ModelViewSet):
    queryset = Usuario.objects.all()
    serializer_class = UsuarioSerializer


class ReservaViewSet(viewsets.ModelViewSet):
    queryset = Reserva.objects.all()
    serializer_class = ReservaSerializer


class ReservaVooViewSet(viewsets.ModelViewSet):
    queryset = ReservaVoo.objects.all()
    serializer_class = ReservaVooSerializer
