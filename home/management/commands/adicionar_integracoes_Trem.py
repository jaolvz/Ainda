from django.core.management.base import BaseCommand
from home.models import Parada

class Command(BaseCommand):
    help = 'Atualiza a integração de trem para paradas de ônibus específicas.'

    def handle(self, *args, **options):
        paradas = [
            {'parada_id': '5149O00193C9', 'estacao_nome': 'Santa Cruz'},
            {'parada_id': '5149O00203C9', 'estacao_nome': 'Santa Cruz'}
        ]

        for parada in paradas:
            try:
                parada_obj = Parada.objects.get(parada_id=parada['parada_id'])
                parada_obj.integracao_trem = True
                parada_obj.estacao_trem = parada['estacao_nome']
                parada_obj.save()
            except Parada.DoesNotExist:
                self.stdout.write(self.style.ERROR(f'BusStop with parada_id {parada["parada_id"]} does not exist'))
