from django.core.management.base import BaseCommand
from home.models import LinhaDeOnibus
import pandas as pd


class Command (BaseCommand):
    help = 'Impostando linha via CSV'

    def add_arguments(self, parser):
        parser.add_argument('csv_file', type=str, help='The path to the CSV file to be imported')

    def handle(self, *args, **kwargs):
        csv_file = kwargs['csv_file']
        
        # Ler o CSV
        df = pd.read_csv(csv_file)

        # Selecionar as colunas de interesse e inserir no banco de dados
        for index, row in df.iterrows():
            LinhaDeOnibus.objects.create(
                rota_id=row['route_id'],
                rota_numero=row['route_short_name'],
                rota_nome=row.get('route_long_name', ''),
                
            )

        self.stdout.write(self.style.SUCCESS('rotas importadas com sucesso'))