# Generated by Django 3.0.6 on 2020-07-04 19:46

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('aplicacao', '0001_initial'),
    ]

    operations = [
        migrations.AlterField(
            model_name='reservavoopassageiro',
            name='tipo_documento',
            field=models.ForeignKey(on_delete=django.db.models.deletion.PROTECT, to='aplicacao.TipoDocumento'),
        ),
    ]