from django.db import models


class Usuario(models.Model):
    nome = models.CharField(max_length=250)
    email = models.CharField(max_length=250)

    def __str__(self):
        return self.nome
