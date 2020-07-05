from rest_framework import serializers
from .models import Usuario, Voo, QuartoHotel, ReservaQuartoHotel, \
    ReservaVoo, ReservaVooPassageiro, \
    TipoDocumento, Reserva, StatusReserva


class UsuarioSerializer(serializers.ModelSerializer):
    class Meta:
        model = Usuario
        fields = '__all__'


class VooSerializer(serializers.ModelSerializer):
    class Meta:
        model = Voo
        fields = '__all__'


class ReservaVooSerializer(serializers.ModelSerializer):
    voos = VooSerializer(many=True)

    class Meta:
        model = ReservaVoo
        fields = ('id', 'voos', 'num_passageiros')

    def create(self, validated_data):
        voos_data = validated_data.pop('voos')
        voos = []
        for voo_data in voos_data:
            voo_object = Voo.objects.create(**voo_data)
            voos.append(voo_object.id)

        reserva_voo = ReservaVoo.objects.create(**validated_data)
        reserva_voo.voos.set(voos)
        return reserva_voo


class ReservaSerializer(serializers.ModelSerializer):
    # voos = VooSerializer(many=True)
    status = serializers.PrimaryKeyRelatedField(
        queryset=StatusReserva.objects.all())
    usuario = serializers.PrimaryKeyRelatedField(
        queryset=Usuario.objects.all())

    class Meta:
        model = Reserva
        fields = '__all__'

    def create(self, validated_data):
        reserva_voo_data = validated_data.pop('reserva_voo')
        reserva_voo = ReservaVooSerializer().create(reserva_voo_data)
        # voos_data = validated_data.pop('voos')
        # voos = []
        # for voo_data in voos_data:
        #     voo_object = Voo.objects.get_or_create(**voo_data)
        #     voos.append(voo_object.id)
        #
        # reserva_voo = ReservaVoo.objects.create(**reserva_voo_data)
        # reserva_voo.voos.set(voos)
        reserva = Reserva.objects.create(**validated_data)
        reserva.reserva_voo = reserva_voo
        return reserva


