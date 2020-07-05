from rest_framework import serializers
from .models import Usuario, Voo, QuartoHotel, ReservaQuartoHotel, \
    ReservaVoo, ReservaVooPassageiro, Reserva, StatusReserva


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
        voos_list = []
        for voo_data in voos_data:
            voo_object = Voo.objects.create(**voo_data)
            voos_list.append(voo_object.id)

        reserva_voo = ReservaVoo.objects.create(**validated_data)
        reserva_voo.voos.set(voos_list)
        return reserva_voo


class QuartoHotelSerializer(serializers.ModelSerializer):
    class Meta:
        model = QuartoHotel
        fields = '__all__'


class ReservaQuartoHotelSerializer(serializers.ModelSerializer):
    quarto_hotel = QuartoHotelSerializer(many=False)

    class Meta:
        model = ReservaQuartoHotel
        fields = '__all__'

    def create(self, validated_data):
        quarto_hotel_data = validated_data.pop('quarto_hotel')
        quarto_hotel_object = QuartoHotel.objects.get_or_create(**quarto_hotel_data)[0]
        reserva_hotel = ReservaQuartoHotel.objects.create(quarto_hotel=quarto_hotel_object, **validated_data)
        return reserva_hotel


class ReservaSerializer(serializers.ModelSerializer):
    # TODO: fazer validação se 1 for null o outro não pode ser
    reserva_voo = ReservaVooSerializer(many=False, required=False)
    hotel_required = False if reserva_voo else True
    reserva_hotel = ReservaQuartoHotelSerializer(many=False, required=hotel_required)

    status = serializers.PrimaryKeyRelatedField(
        queryset=StatusReserva.objects.all())
    usuario = serializers.PrimaryKeyRelatedField(
        queryset=Usuario.objects.all())

    class Meta:
        model = Reserva
        fields = ['id', 'usuario', 'telefone_contato',
                  'reserva_voo', 'reserva_hotel', 'seguro_viagem',
                  'valor_total', 'parcelas', 'status']

    def create(self, validated_data):

        reserva_voo_obj, reserva_hotel_obj = None, None

        if 'reserva_voo' in validated_data:
            reserva_voo_data = validated_data.pop('reserva_voo')
            voos_data = reserva_voo_data.pop('voos')
            reserva_voo_obj = ReservaVoo.objects.create(**reserva_voo_data)
            voos_ids = []
            for voo_data in voos_data:
                voo_object = Voo.objects.get_or_create(**voo_data)[0]
                voos_ids.append(voo_object.id)
            reserva_voo_obj.voos.set(voos_ids)
        if 'reserva_hotel' in validated_data:
            reserva_hotel_data = validated_data.pop('reserva_hotel')
            quarto_hotel_data = reserva_hotel_data.pop('quarto_hotel')
            quarto_hotel_obj = QuartoHotel.objects.get_or_create(**quarto_hotel_data)[0]
            reserva_hotel_obj = ReservaQuartoHotel.objects.create(quarto_hotel=quarto_hotel_obj, **reserva_hotel_data)

        reserva = Reserva.objects.create(reserva_voo=reserva_voo_obj,
                                         reserva_hotel=reserva_hotel_obj,
                                         **validated_data)

        return reserva
