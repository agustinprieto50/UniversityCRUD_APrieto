from django.db import models
from django.db.models.fields import CharField

# Create your models here.

class Curso(models.Model):
    codigo = CharField(primary_key=True, max_length=6)
    nombre = CharField(max_length=50)
    creditos = models.PositiveSmallIntegerField()

    def __str__(self):
        texto = f"{self.nombre} ({self.creditos})"
        return texto