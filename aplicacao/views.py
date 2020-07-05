from django.shortcuts import render
from rest_framework import viewsets, generics
from .models import Usuario, Reserva
from .serializers import UsuarioSerializer, ReservaSerializer


class UsuarioViewSet(viewsets.ModelViewSet):
    queryset = Usuario.objects.all()
    serializer_class = UsuarioSerializer


class ReservaViewSet(viewsets.ModelViewSet):
    queryset = Reserva.objects.all()
    serializer_class = ReservaSerializer


class UsuarioReservaList(generics.ListAPIView):
    serializer_class = ReservaSerializer

    def get_queryset(self):
        cpf = self.kwargs['cpf']
        return Reserva.objects.filter(usuario__cpf=cpf)
