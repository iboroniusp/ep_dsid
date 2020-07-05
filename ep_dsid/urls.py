from django.contrib import admin
from django.urls import path, include
from aplicacao.views import UsuarioViewSet, ReservaViewSet
from rest_framework import routers

router = routers.DefaultRouter()
router.register(r'usuario', UsuarioViewSet)
router.register(r'reserva', ReservaViewSet)

urlpatterns = [
    path('', include(router.urls)),
    path('admin/', admin.site.urls),
    path('api-auth/', include('rest_framework.urls')),

]
