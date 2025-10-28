from django.shortcuts import render
from rest_framework import viewsets
from .models import Funcionarios, Hospedes, Quartos, Reservas, Relatorios
from .serializers import FuncionariosSerializer, HospedesSerializer, QuartosSerializer, ReservasSerializer, RelatoriosSerializer
# Create your views here.

class FuncionariosViewSet(viewsets.ModelViewSet):
    queryset = Funcionarios.objects.all()
    serializer_class = FuncionariosSerializer

class HospedesViewSet(viewsets.ModelViewSet):
    queryset = Hospedes.objects.all()
    serializer_class = HospedesSerializer

class QuartosViewSet(viewsets.ModelViewSet):
    queryset = Quartos.objects.all()
    serializer_class = QuartosSerializer

class ReservasViewSet(viewsets.ModelViewSet):
    queryset = Reservas.objects.all()
    serializer_class = ReservasSerializer

class RelatoriosViewSet(viewsets.ModelViewSet):
    queryset = Relatorios.objects.all()
    serializer_class = RelatoriosSerializer

