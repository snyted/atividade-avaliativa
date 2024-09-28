from django.db import models

class Equipamentos(models.Model):
    equipamento = models.CharField(max_length=100)
    quantidade = models.IntegerField()

    def __str__(self) -> str:
        return self.equipamento