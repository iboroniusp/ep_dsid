from django.contrib import admin
from django.urls import path, include
from aplicacao.views import UsuarioViewSet, \
    ReservaByUsuarioId, ReservaByUsuarioCpf, \
    ReservaViewSet, UsuariosByEmailSenha
from rest_framework import routers

router = routers.DefaultRouter()
router.register(r'usuarios', UsuarioViewSet)
router.register(r'reservas', ReservaViewSet)

urlpatterns = [
    path('', include(router.urls)),
    path('admin/', admin.site.urls),
    path('api-auth/', include('rest_framework.urls')),
    path('usuarios/cpf/<str:cpf>/reservas/', ReservaByUsuarioCpf.as_view(), name='usuario-cpf-reservas'),
    path('usuarios/id/<int:id>/reservas/', ReservaByUsuarioId.as_view(), name='usuario-id-reservas'),
    path('usuarios/email=<str:email>&senha=<str:senha>/', UsuariosByEmailSenha.as_view(), name='login'),
]
