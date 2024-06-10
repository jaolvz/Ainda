from django.core.management.base import BaseCommand
from home.models import Disponibilidade
import pandas as pd


class Command (BaseCommand):
    help = 'Importando calendário via CSV'

    def add_arguments(self, parser):
        parser.add_argument('csv_file', type=str, help='The path to the CSV file to be imported')

    def handle(self, *args, **kwargs):
        csv_file = kwargs['csv_file']
        
        # Ler o CSV
        df = pd.read_csv(csv_file)

        # Selecionar as colunas de interesse e inserir no banco de dados
        for index, row in df.iterrows():
            Disponibilidade.objects.create(
            service_id=row['service_id'],
            segunda=row['monday'],
            terca=row['tuesday'],
            quarta=row['wednesday'],
            quinta=row['thursday'],
            sexta=row['friday'],
            sabado=row['saturday'],
            domingo=row['sunday'],

            )

        self.stdout.write(self.style.SUCCESS('disponibilidade importada com sucesso'))