# Generated by Django 4.2.13 on 2024-06-13 09:25

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('home', '0009_viagem_destino_id'),
    ]

    operations = [
        migrations.AddField(
            model_name='parada',
            name='estacao_trem',
            field=models.CharField(blank=True, max_length=255, null=True),
        ),
        migrations.AddField(
            model_name='parada',
            name='integracao_trem',
            field=models.BooleanField(default=False),
        ),
    ]
