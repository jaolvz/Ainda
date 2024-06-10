from django.core.management.base import BaseCommand
from home.models import  Parada
import pandas as pd


class Command (BaseCommand):
    help = 'Importando paradas via CSV'

    def add_arguments(self, parser):
        parser.add_argument('csv_file', type=str, help='The path to the CSV file to be imported')

    def handle(self, *args, **kwargs):
        csv_file = kwargs['csv_file']
        
        # Ler o CSV
        df = pd.read_csv(csv_file)

        # Selecionar as colunas de interesse e inserir no banco de dados
        for index, row in df.iterrows():
            Parada.objects.create(
                parada_id=row['stop_id'],
                referencia_parada=row['stop_name'],
                parada_latitude=row['stop_lat'],
                parada_longitude=row['stop_lon']

            )

        self.stdout.write(self.style.SUCCESS('paradas importadas com sucesso'))