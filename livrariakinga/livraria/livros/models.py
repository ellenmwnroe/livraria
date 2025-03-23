from django.db import models

# Create your models here.
from django.db import models

class Livro(models.Model):
    titulo = models.CharField(max_length=255)
    genero = models.CharField(max_length=100)
    quantidade = models.IntegerField()

    def __str__(self):
        return f'{self.titulo} - {self.genero}'
