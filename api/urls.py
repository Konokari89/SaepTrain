from django.contrib import admin
from django.urls import path, include
from rest_framework import routers
from .views import FuncionariosViewSet, HospedesViewSet, QuartosViewSet, ReservasViewSet, RelatoriosViewSet

routers = routers.DefaultRouter()

routers.register(r'funcionarios', FuncionariosViewSet)
routers.register(r'hospedes', HospedesViewSet)
routers.register(r'quartos', QuartosViewSet)
routers.register(r'reservas', ReservasViewSet)
routers.register(r'relatorios', RelatoriosViewSet)

urlpatterns = [
    path('admin/', admin.site.urls),
    path('api/', include(routers.urls)),
]