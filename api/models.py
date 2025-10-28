from django.db import models

# Create your models here.
class Funcionarios(models.Model):
    id = models.AutoField(primary_key=True)
    login = models.CharField(max_length=50, unique=True)
    senha = models.CharField(max_length=100)
    nome = models.CharField(max_length=100)
    sobrenome = models.CharField(max_length=100)
    cpf = models.CharField(max_length=14, unique=True)
    turno = models.CharField(max_length=20)
    cargo = models.CharField(max_length=50)
    
    class Meta:
        db_table = 'funcionarios'
    

class Hospedes(models.Model):
    id_hospede = models.AutoField(primary_key=True)
    nome = models.CharField(max_length=100)
    sobrenome = models.CharField(max_length=100)
    cpf = models.CharField(max_length=14, unique=True)
    telefone = models.CharField(max_length=15)
    idade = models.IntegerField()

    class Meta:
        db_table = 'hospedes'

class Quartos(models.Model):
    num_quarto = models.IntegerField(primary_key=True)
    disponibilidade = models.BooleanField(default=True)
    tipo = models.CharField(max_length=50)
    valor_diaria = models.DecimalField(max_digits=10, decimal_places=2)
    fk_id_hospede = models.ForeignKey(Hospedes, on_delete=models.SET_NULL, null=True, blank=True)
    class Meta:
        db_table = 'quartos'

class Reservas(models.Model):
    id_resrva = models.AutoField(primary_key=True)
    fk_id_hospede = models.ForeignKey(Hospedes, on_delete=models.CASCADE)
    fk_num_quarto = models.ForeignKey(Quartos, on_delete=models.CASCADE)
    data_inicio = models.DateField()
    data_fim = models.DateField()
    status = models.CharField(max_length=20)

    class Meta:
        db_table = 'reservas'

class Relatorios(models.Model):
    id_relatorio = models.AutoField(primary_key=True)
    fk_id_funcionario = models.ForeignKey(Funcionarios, on_delete=models.CASCADE)
    data_criacao = models.DateField(auto_now_add=True)
    conteudo = models.TextField()
    fk_id_reserva = models.ForeignKey(Reservas, on_delete=models.CASCADE)
    fk_id_quarto = models.ForeignKey(Quartos, on_delete=models.CASCADE)
    fk_id_hospede = models.ForeignKey(Hospedes, on_delete=models.CASCADE)


    class Meta:
        db_table = 'relatorios'

