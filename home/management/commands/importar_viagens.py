from django.core.management.base import BaseCommand
from home.models import Viagem
import pandas as pd


class Command (BaseCommand):
    help = 'Importando viagens via CSV'

    def add_arguments(self, parser):
        parser.add_argument('csv_file', type=str, help='The path to the CSV file to be imported')

    def handle(self, *args, **kwargs):
        csv_file = kwargs['csv_file']
        
        # Ler o CSV
        df = pd.read_csv(csv_file)

        # Selecionar as colunas de interesse e inserir no banco de dados
        for index, row in df.iterrows():
            Viagem.objects.create(
                viagem_id=row['trip_id'],
                rota=row['route_id'],
                service =row['service_id'],
                destino_letreiro=row['trip_headsign'],
                rota_numero=row['trip_short_name'],


            )

        self.stdout.write(self.style.SUCCESS('viagens importadas com sucesso'))