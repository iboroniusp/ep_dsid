from django.db import models

default_char = ""
default_number = 0


class Usuario(models.Model):
    nome = models.CharField(max_length=250, default=default_char)
    email = models.CharField(max_length=200, default=default_char)
    senha = models.CharField(max_length=50, default=default_char)
    cpf = models.CharField(max_length=11, default=default_char)

    def __str__(self):
        return self.nome


class Voo(models.Model):
    id_voo = models.BigIntegerField()
    nome_companhia = models.CharField(max_length=200, default=default_char)
    classe = models.CharField(max_length=200, default=default_char)
    data_voo = models.DateTimeField()
    aeroporto_origem = models.CharField(max_length=500, default=default_char)
    aeroporto_destino = models.CharField(max_length=500, default=default_char)
    pais_origem = models.CharField(max_length=100, default=default_char)
    pais_destino = models.CharField(max_length=100, default=default_char)
    valor_total = models.DecimalField(max_digits=10, decimal_places=2)
    max_passageiros = models.IntegerField(default=200)
    cheio = models.BooleanField(default=False)

    def __str__(self):
        return f"Voo {self.id} de {self.aeroporto_origem} para {self.aeroporto_destino} em {self.data_voo}"


class QuartoHotel(models.Model):
    id_quarto_hotel = models.BigIntegerField()
    nome_hotel = models.CharField(max_length=200, default=default_char)
    nome_quarto = models.CharField(max_length=200, default=default_char)
    descricao_quarto = models.TextField(max_length=500)
    endereco = models.CharField(max_length=350, default=default_char)
    cidade = models.CharField(max_length=350, default=default_char)
    estado = models.CharField(max_length=350, default=default_char)
    pais = models.CharField(max_length=350, default=default_char)
    valor_diaria = models.DecimalField(max_digits=10, decimal_places=2)
    max_hospedes = models.IntegerField()
    disponivel = models.BooleanField(default=True)

    def __str__(self):
        return f"{self.nome_quarto} em {self.nome_hotel}"


class StatusReserva(models.Model):
    status = models.CharField(max_length=50)

    def __str__(self):
        return self.status


class ReservaVoo(models.Model):
    voos = models.ManyToManyField(Voo)
    num_passageiros = models.IntegerField(default=1)

    def __str__(self):
        return str(self.id)


class TipoDocumento(models.Model):
    tipo = models.CharField(max_length=10)

    def __str__(self):
        return self.tipo


class ReservaVooPassageiro(models.Model):
    nome = models.CharField(max_length=150)
    ultimo_sobrenome = models.CharField(max_length=100)
    tipo_documento = models.ForeignKey(TipoDocumento, on_delete=models.PROTECT)
    documento = models.CharField(max_length=11)
    voo = models.ForeignKey(ReservaVoo, on_delete=models.CASCADE)

    def __str__(self):
        return f"{self.ultimo_sobrenome}, {self.nome} - Voo: {self.voo.id}"


class ReservaQuartoHotel(models.Model):
    data_entrada = models.DateTimeField()
    data_saida = models.DateTimeField()
    hospede_principal = models.BooleanField(default=True)
    nome_hospede_principal = models.CharField(max_length=250, default=default_char)
    qtd_hospedes = models.IntegerField()
    quarto_hotel = models.ForeignKey(QuartoHotel, on_delete=models.CASCADE)

    def __str__(self):
        return f"Reserva {self.id} - Quarto {self.quarto_hotel.id}"


# reservar um pacote neste caso nada mais é que selecionar um quarto e um voo
class Reserva(models.Model):
    usuario = models.ForeignKey(Usuario, on_delete=models.PROTECT)
    telefone_contato = models.CharField(max_length=11, default=default_char)
    reserva_voo = models.OneToOneField(ReservaVoo, on_delete=models.CASCADE, null=True, related_name="reserva_voo")
    reserva_hotel = models.OneToOneField(ReservaQuartoHotel, on_delete=models.CASCADE, null=True, blank=True)
    valor_total = models.DecimalField(max_digits=10, decimal_places=2)
    data_reserva = models.DateTimeField(auto_now=True)

    def __str__(self):
        return str(self.id)
