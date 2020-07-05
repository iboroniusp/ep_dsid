# Generated by Django 3.0.6 on 2020-07-05 15:27

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('aplicacao', '0003_auto_20200705_0028'),
    ]

    operations = [
        migrations.AlterField(
            model_name='reserva',
            name='reserva_hotel',
            field=models.OneToOneField(blank=True, null=True, on_delete=django.db.models.deletion.CASCADE, to='aplicacao.ReservaQuartoHotel'),
        ),
        migrations.AlterField(
            model_name='reserva',
            name='reserva_voo',
            field=models.OneToOneField(null=True, on_delete=django.db.models.deletion.CASCADE, related_name='reserva_voo', to='aplicacao.ReservaVoo'),
        ),
    ]