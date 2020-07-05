from rest_framework import serializers
from .models import Usuario, Voo, QuartoHotel, ReservaQuartoHotel, \
    ReservaVoo, Pagamento, ReservaVooPassageiro, \
    TipoDocumento, Reserva, StatusReserva


class UsuarioSerializer(serializers.ModelSerializer):
    class Meta:
        model = Usuario
        fields = '__all__'

#
# class VooSerializer(serializers.ModelSerializer):
#     id_voo = models.BigIntegerField()
#     nome_companhia = models.CharField(max_length=200, default=default_char)
#     classe = models.CharField(max_length=200, default=default_char)
#     data_voo = models.DateTimeField()
#     aeroporto_origem = models.CharField(max_length=5, default=default_char)
#     aeroporto_destino = models.CharField(max_length=5, default=default_char)
#     pais_origem = models.CharField(max_length=100, default=default_char)
#     pais_destino = models.CharField(max_length=100, default=default_char)
#     valor_total = models.DecimalField(max_digits=10, decimal_places=2)
#     max_passageiros = models.IntegerField(default=200)
#     cheio = models.BooleanField(default=False)
#
#     def __str__(self):
#         return f"Voo {self.id} de {self.aeroporto_origem} para {self.aeroporto_destino} em {self.data_voo}"
#
#
# class QuartoHotelSerializer(serializers.ModelSerializer):
#     id_quarto_hotel = models.BigIntegerField()
#     nome_hotel = models.CharField(max_length=200, default=default_char)
#     nome_quarto = models.CharField(max_length=200, default=default_char)
#     descricao_quarto = models.TextField(max_length=500)
#     endereco = models.CharField(max_length=350, default=default_char)
#     cidade = models.CharField(max_length=350, default=default_char)
#     estado = models.CharField(max_length=350, default=default_char)
#     pais = models.CharField(max_length=350, default=default_char)
#     valor_diaria = models.DecimalField(max_digits=10, decimal_places=2)
#     max_hospedes = models.IntegerField()
#     disponivel = models.BooleanField(default=True)
#
#     def __str__(self):
#         return f"{self.nome_quarto} em {self.nome_hotel}"
#
#
# class PagamentoSerializer(serializers.ModelSerializer):
#     valor_total = models.DecimalField(max_digits=10, decimal_places=2)
#     parcelas = models.IntegerField()
#
#     def __str__(self):
#         return str(self.id)
#
#
# class ReservaVooSerializer(serializers.ModelSerializer):
#     voo = models.ManyToManyField(Voo)
#     passageiros = models.IntegerField(default=1)
#
#     def __str__(self):
#         return str(self.id)
#
#
# class ReservaVooPassageiroSerializer(serializers.ModelSerializer):
#     nome = models.CharField(max_length=150)
#     ultimo_sobrenome = models.CharField(max_length=100)
#     tipo_documento = models.ForeignKey(TipoDocumento, on_delete=models.PROTECT)
#     documento = models.CharField(max_length=11)
#     voo = models.ForeignKey(ReservaVoo, on_delete=models.CASCADE)
#
#     def __str__(self):
#         return f"{self.ultimo_sobrenome}, {self.nome} - Voo: {self.voo.id}"
#
#
# class ReservaQuartoHotelSerializer(serializers.ModelSerializer):
#     data_entrada = models.DateTimeField()
#     data_saida = models.DateTimeField()
#     hospede_principal = models.BooleanField()
#     nome_hospede_principal = models.CharField(max_length=250, default=default_char)
#     # aqui se hospede_principal for marcado, ja preencher automaticamente com o nome do usuario
#     cafe_da_manha = models.BooleanField()
#     viagem_trabalho = models.BooleanField()
#     qtd_hospedes = models.IntegerField()
#     quarto_hotel = models.OneToOneField(QuartoHotel, on_delete=models.CASCADE)
#
#     def __str__(self):
#         return f"Reserva {self.id} - Quarto {self.quarto_hotel.id}"
#
#
# # reservar um pacote neste caso nada mais é que selecionar um quarto e um voo
# class ReservaSerializer(serializers.ModelSerializer):
#     usuario = models.OneToOneField(Usuario, on_delete=models.CASCADE)
#     telefone_contato = models.CharField(max_length=11, default=default_char)
#     reserva_voo = models.OneToOneField(ReservaVoo, on_delete=models.CASCADE, null=True)
#     reserva_hotel = models.OneToOneField(ReservaQuartoHotel, on_delete=models.CASCADE, null=True)
#     seguro_viagem = models.BooleanField()
#     pgto = models.OneToOneField(Pagamento, on_delete=models.CASCADE)
#     status = models.OneToOneField(StatusReserva, on_delete=models.PROTECT)
#
#     def __str__(self):
#         return str(self.id)

