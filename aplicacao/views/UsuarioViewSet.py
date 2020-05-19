from django.shortcuts import render
from rest_framework import viewsets
from ..models.Usuario import Usuario
from ..serializers.UsuarioSerializer import UsuarioSerializer


class UsuarioViewSet(viewsets.ModelViewSet):
    queryset = Usuario.objects.all()
    serializer_class = UsuarioSerializer
