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


class ReservaByUsuarioCpf(generics.ListAPIView):
    serializer_class = ReservaSerializer

    def get_queryset(self):
        cpf = self.kwargs['cpf']
        return Reserva.objects.filter(usuario__cpf=cpf)


class ReservaByUsuarioId(generics.ListAPIView):
    serializer_class = ReservaSerializer

    def get_queryset(self):
        id = self.kwargs['id']
        return Reserva.objects.filter(usuario__id=id)


class UsuariosByEmailSenha(generics.ListAPIView):
    serializer_class = UsuarioSerializer

    def get_queryset(self):
        email = self.kwargs['email']
        senha = self.kwargs['senha']
        return Usuario.objects.filter(email=email, senha=senha)
