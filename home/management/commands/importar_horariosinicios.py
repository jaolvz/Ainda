from django.core.management.base import BaseCommand
from home.models import Horario_Inicio
import pandas as pd

class Command(BaseCommand):
    help = 'Importando horários_inicio via CSV'

    def add_arguments(self, parser):
        parser.add_argument('csv_file', type=str, help='The path to the CSV file to be imported')

    def handle(self, *args, **kwargs):
        csv_file = kwargs['csv_file']
        
        # Ler o CSV em pedaços (chunksize)
        chunksize = 1000  # Experimente diferentes tamanhos de pedaço para encontrar o mais eficiente
        for chunk in pd.read_csv(csv_file, chunksize=chunksize):
            # Selecionar as colunas de interesse e inserir no banco de dados
            bulk_instances = []
            for index, row in chunk.iterrows():
                instance = Horario_Inicio(
                    viagem_id=row['trip_id'],
                    horario=row['start_time'],
                )
                bulk_instances.append(instance)

            # Inserir instâncias em massa no banco de dados
            Horario_Inicio.objects.bulk_create(bulk_instances)

        self.stdout.write(self.style.SUCCESS('horários importadas com sucesso'))
