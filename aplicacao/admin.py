from django.contrib import admin
from .models import Usuario, Voo, QuartoHotel, ReservaQuartoHotel, ReservaVoo, Pagamento

admin.site.register(Usuario)
admin.site.register(Voo)
admin.site.register(QuartoHotel)
admin.site.register(ReservaVoo)
admin.site.register(ReservaQuartoHotel)
admin.site.register(Pagamento)

