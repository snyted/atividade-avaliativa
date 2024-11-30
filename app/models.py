from django.db import models

class Equipamentos(models.Model):
    equipamento = models.CharField(max_length=100)
    quantidade = models.IntegerField()

    def __str__(self) -> str:
        return self.equipamento
    
class Cadastro_Colaboradores(models.Model):
    colaborador = models.CharField(max_length=100)
    matricula = models.CharField(max_length=20)
    senha = models.CharField(max_length=100)

    def __str__(self) -> str:
        return self.colaborador
    
class Acoes(models.Model):
    colaborador = models.ForeignKey(Cadastro_Colaboradores, on_delete=models.CASCADE)
    equipamento = models.ForeignKey(Equipamentos, on_delete=models.CASCADE)
    dataEmprestimo = models.DateField()
    dataDevolucao = models.DateField()
    status = models.CharField(max_length=100)
    condicoes = models.CharField(max_length=100)
    dataDevolucaoReal = models.DateField(null=True, blank=True)
    observacoes = models.TextField()
    
    def __str__(self) -> str:
        return f'Ação: {self.colaborador} - {self.equipamento} ({self.status})'