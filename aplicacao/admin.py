from django.contrib import admin
from .models import Usuario, Voo, QuartoHotel, ReservaQuartoHotel, \
    ReservaVoo, Pagamento, ReservaVooPassageiro, \
    TipoDocumento, Reserva, StatusReserva

admin.site.register(Usuario)
admin.site.register(Voo)
admin.site.register(QuartoHotel)
admin.site.register(ReservaVoo)
admin.site.register(ReservaVooPassageiro)
admin.site.register(TipoDocumento)
admin.site.register(ReservaQuartoHotel)
admin.site.register(Reserva)
admin.site.register(StatusReserva)
admin.site.register(Pagamento)

# NO BANCO:
# para voo:
# quando o cliente clicar em confirmar compra
# -> insere dados do voo no banco (se já não houver), recupera o id desse voo
# -> insere uma nova reserva de voo e recupera esse id
# -> insere os passageiros com o id dessa reserva de voo
# -> insere uma reserva com o id desse voo, mas com o id do quarto null
#
#
# para quarto de hotel:
# quando o cliente clicar em confirmar compra
# -> insere dados do quarto no banco (se já não houver), recupera o id desse voo
# -> insere uma nova reserva de quarto e recupera esse id
# -> insere uma reserva com o id desse quarto, mas com o id do voo null
#
#
# para pacote:
# quando o cliente clicar em confirmar compra
# -> faz o processo do quarto
# -> faz o processo do voo
# * o id da reserva é o mesmo neste caso então tanto o id do quarto quanto id do voo são preenchidos com o que foi recuperado
# ###