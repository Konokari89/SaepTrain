from rest_framework import serializers
from .models import Hospedes, Quartos, Reservas, Funcionarios, Relatorios


class HospedesSerializer(serializers.ModelSerializer):
    class Meta:
        model = Hospedes
        fields = '__all__'
        read_only_fields = ['id_hospede']

class QuartosSerializer(serializers.ModelSerializer):
    class Meta:
        model = Quartos
        fields = '__all__'
        read_only_fields = ['num_quarto']
        read_only_fields = ['id_relatorio']

class ReservasSerializer(serializers.ModelSerializer):
    class Meta:
        model = Reservas
        fields = '__all__'
        read_only_fields = ['id_resrva']

class FuncionariosSerializer(serializers.ModelSerializer):
    class Meta:
        model = Funcionarios
        fields = '__all__'
        read_only_fields = ['id_funcionario']
        


class RelatoriosSerializer(serializers.ModelSerializer):
    class Meta:
        model = Relatorios
        fields = '__all__'
        read_only_fields = ['id_relatorio']

