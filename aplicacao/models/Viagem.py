from django.db import models


class Viagem(models.Model):
    data = models.DateTimeField()
    origem = models.CharField(max_length=250)
    destino = models.CharField(max_length=250)

    def __str__(self):
        return self.origem, self.destino
