from django.contrib import admin
from django.urls import path, include
from aplicacao.views import UsuarioViewSet, UsuarioReservaList, ReservaViewSet
from rest_framework import routers

router = routers.DefaultRouter()
router.register(r'usuarios', UsuarioViewSet)
router.register(r'reservas', ReservaViewSet)
#router.register(r'^usuarios/{cpf}/reservas/$', UsuarioReservaList.as_view(), basename='usuarioreservas'),

urlpatterns = [
    path('', include(router.urls)),
    path('admin/', admin.site.urls),
    path('api-auth/', include('rest_framework.urls')),
]
