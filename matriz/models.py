from django.db import models

# Create your models here.
class Matriz(models.Model):
    nome = models.CharField(max_length=50)
    ano = models.DateField()
    status = models.BooleanField()
    carga_horaria = models.FloatField()

    def __str__(self):
        return self.nome
