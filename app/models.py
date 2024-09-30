from django.db import models

class Equipamentos(models.Model):
    equipamento = models.CharField(max_length=100)
    quantidade = models.IntegerField()

    def __str__(self) -> str:
        return self.equipamento
    
class Cadastro_Colaboradores(models.Model):
    colaborador = models.CharField(max_length=100)
    matricula = models.CharField(max_length=100)
    senha = models.CharField(max_length=100)

    def __str__(self) -> str:
        return self.colaborador