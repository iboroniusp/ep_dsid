from django.db import models

default_char = ""


class Usuario(models.Model):
    nome = models.CharField(max_length=200, default=default_char)
    email = models.CharField(max_length=200, default=default_char)
    senha = models.CharField(max_length=50, default=default_char)
    cpf = models.CharField(max_length=11, default=default_char)

    def __str__(self):
        return self.nome


class Voo(models.Model):
    nome_companhia = models.CharField(max_length=200, default=default_char)
    classe = models.CharField(max_length=200, default=default_char)
    data_voo = models.CharField(max_length=50, default=default_char)
    origem = models.CharField(max_length=11, default=default_char)
    destino = models.CharField(max_length=11, default=default_char)
    max_passageiros = models.IntegerField()
    cheio = models.BooleanField()

    def __str__(self):
        return f"Voo num. {self.id_voo} from {self.origem} to {self.destino} at {self.data_voo}"


class QuartoHotel(models.Model):
    nome_hotel = models.CharField(max_length=200, default=default_char)
    nome_quarto = models.CharField(max_length=200, default=default_char)
    descricao_quarto = models.TextField(max_length=500)
    max_hospedes = models.IntegerField()
    disponivel = models.BooleanField()

    def __str__(self):
        return f"{self.nome_quarto} em {self.nome_hotel}"


class Pagamento(models.Model):
    status = models.CharField(max_length=50, default=default_char)
    valor_total = models.DecimalField(max_digits=10, decimal_places=2)
    parcelas = models.IntegerField()


# class ReservaPassageiros(models.Model):
#     id_reserva_pass = models.BigIntegerField()
#     nome = models.CharField(max_length=100)
#     ultimo_sobrenome = models.CharField(max_length=100)
#     cpf = models.CharField(max_length=11)
#     rg = models.CharField(max_length=10)
#     passaporte = models.CharField(max_length=8)


class ReservaVoo(models.Model):
    telefone_contato = models.CharField(max_length=11, default=default_char)
    usuario = models.OneToOneField(Usuario, on_delete=models.CASCADE)
    voo = models.ManyToManyField(Voo)
    pgto = models.OneToOneField(Pagamento, on_delete=models.CASCADE)
    # relação 1:N  com passageiros


class ReservaQuartoHotel(models.Model):
    data_entrada = models.DateTimeField()
    data_saida = models.DateTimeField()
    hospede_principal = models.BooleanField()
    nome_hospede_principal = models.CharField(max_length=100, default=default_char)
    # aqui se hospede_principal for marcado, ja preencher automaticamente com o nome do usuario
    cafe_da_manha = models.BooleanField()
    viagem_trabalho = models.BooleanField()
    qtd_hospedes = models.IntegerField()
    telefone_contato = models.CharField(max_length=11, default=default_char)
    usuario = models.OneToOneField(Usuario, on_delete=models.CASCADE)
    quarto_hotel = models.OneToOneField(QuartoHotel, on_delete=models.CASCADE)
    pgto = models.OneToOneField(Pagamento, on_delete=models.CASCADE)


# class ReservaPacote(models.Model):
#     # 1:1 com quartoe de hotel e voo