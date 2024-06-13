from django.core.management.base import BaseCommand
from home.models import Parada

class Command(BaseCommand):
    help = 'Atualiza a integração de metro para paradas de ônibus específicas.'

    def handle(self, *args, **options):
        paradas = [
            {'parada_id': '1008O00025S0', 'estacao_nome': 'Cidade Nova'},
            {'parada_id': '1008O00006S0', 'estacao_nome': 'Cidade Nova'},
            {'parada_id': '1008O00002S0', 'estacao_nome': 'Cidade Nova'},
            {'parada_id': '1008O00030S0', 'estacao_nome': 'Cidade Nova'},
            {'parada_id': '1008O00003S2', 'estacao_nome': 'Cidade Nova'},
            {'parada_id': '1008O00017S0', 'estacao_nome': 'Cidade Nova'},
            {'parada_id': '1008O00022S0', 'estacao_nome': 'Cidade Nova'},
            #Praça Onze
            {'parada_id': '1008O00018S0', 'estacao_nome': 'Praça Onze'},
            {'parada_id': '1008O00001S0', 'estacao_nome': 'Praça Onze'},
            {'parada_id': '1008O00023S0', 'estacao_nome': 'Praça Onze'},
            {'parada_id': '1008O00024S0', 'estacao_nome': 'Praça Onze'},
            {'parada_id': '1008O00026S0', 'estacao_nome': 'Praça Onze'},
            {'parada_id': '1008O00027S0', 'estacao_nome': 'Praça Onze'},
            {'parada_id': '1008O00005S0', 'estacao_nome': 'Praça Onze'},
            {'parada_id': '1008O00007S0', 'estacao_nome': 'Praça Onze'},
            {'parada_id': '1008O00004S0', 'estacao_nome': 'Praça Onze'},
            {'parada_id': '1008O00033C0', 'estacao_nome': 'Praça Onze'},
            {'parada_id': '1008O00019S0', 'estacao_nome': 'Praça Onze'},
             #São Cristóvão
              {'parada_id': '1010O00078C0', 'estacao_nome': 'São Cristovão'},
              {'parada_id': '1010O00103C0', 'estacao_nome': 'São Cristovão'},
              {'parada_id': '2035O00059C0', 'estacao_nome': 'São Cristovão'},
              {'parada_id': '2035O00049C0', 'estacao_nome': 'São Cristovão'},   
              {'parada_id': '2035O00078C0', 'estacao_nome': 'São Cristovão'},
             #Siqueira Campos
             {'parada_id': 'zmv1', 'estacao_nome': 'Siqueira Campos'},
             {'parada_id': '2024O00105C0', 'estacao_nome': 'Siqueira Campos'},
             {'parada_id': '2024O00022C0', 'estacao_nome': 'Siqueira Campos'},
             {'parada_id': '2024O00095C0', 'estacao_nome': 'Siqueira Campos'},
            #Estácio
             {'parada_id': '1008O00042C0', 'estacao_nome': 'Estácio'},
            {'parada_id': '1009O00004S9', 'estacao_nome': 'Estácio'},
             {'parada_id': '1009O00010S9', 'estacao_nome': 'Estácio'},
             #Triagem
             {'parada_id': '1012O00028C0', 'estacao_nome': 'Triagem'},
             #Jardim Oceanico
             {'parada_id': '4128O00109C0', 'estacao_nome': 'Jardim Oceânico'},
             {'parada_id': '4128O00138C0', 'estacao_nome': 'Jardim Oceânico'},
             {'parada_id': '4128O00173C0', 'estacao_nome': 'Jardim Oceânico'},
            {'parada_id': '4128BO0019T9', 'estacao_nome': 'Jardim Oceânico'},
            {'parada_id': '4128BO0019P2', 'estacao_nome': 'Jardim Oceânico'},
            {'parada_id': '4128BO0019P1', 'estacao_nome': 'Jardim Oceânico'},
            #São Conrado
            {'parada_id': '2031O00028C0', 'estacao_nome': 'São Conrado/Rocinha'},
            {'parada_id': '2031L00020C0', 'estacao_nome': 'São Conrado/Rocinha'},
            {'parada_id': '2031O00019C0', 'estacao_nome': 'São Conrado/Rocinha'},
            {'parada_id': '2031O00009C0', 'estacao_nome': 'São Conrado/Rocinha'},
            {'parada_id': '2031O00018C0', 'estacao_nome': 'São Conrado/Rocinha'},
            #Antero de Quental
            {'parada_id': '2026O00095C0', 'estacao_nome': 'Antero de Quental'},
            {'parada_id': '2026O00076C0', 'estacao_nome': 'Antero de Quental'},  
               {'parada_id': '2026O00052S0', 'estacao_nome': 'Antero de Quental'}, 
            #Jardim de Alah 
            {'parada_id': '2026O00091C0', 'estacao_nome': 'Jardim de Alah'}, 
             {'parada_id': '2026O00008S0', 'estacao_nome': 'Jardim de Alah'},  
             #Nossa Senhora da Paz
             {'parada_id': '2025O00036S0', 'estacao_nome': 'Nossa Senhora da Paz'},
             {'parada_id': '2025O00035S0', 'estacao_nome': 'Nossa Senhora da Paz'},
            #General Osório
            {'parada_id': '2025O00031C0', 'estacao_nome': 'General Osório'},
            {'parada_id': '2025O00038C0', 'estacao_nome': 'General Osório'},
            {'parada_id': '2025O00020S0', 'estacao_nome': 'General Osório'},
            #Cantagalo
            {'parada_id': '2024O00025C0', 'estacao_nome': 'Cantagalo'},
            {'parada_id': '2024O00093S0', 'estacao_nome': 'Cantagalo'},
              #Cardeal Arcoverde
            {'parada_id': '2024O00123C0', 'estacao_nome': 'Cardeal Arcoverde'},
           {'parada_id': '2024O00027S0', 'estacao_nome': 'Cardeal Arcoverde'},
            #Botafogo
            {'parada_id': '2020O00140C0', 'estacao_nome': 'Botafogo'},
            {'parada_id': '2020O00141C0', 'estacao_nome': 'Botafogo'},
           {'parada_id': '2020O00059S0', 'estacao_nome': 'Botafogo'}, 

           #Flamengo
           {'parada_id': '2015O00060C0', 'estacao_nome': 'Flamengo'}, 
           #Largo do Machado
           {'parada_id': '2018O00010C0', 'estacao_nome': 'Largo do Machado'}, 
            {'parada_id': '2018O00011C0', 'estacao_nome': 'Largo do Machado'}, 
              {'parada_id': '2018O00024C0', 'estacao_nome': 'Largo do Machado'},
               {'parada_id': '2018O00033C0', 'estacao_nome': 'Largo do Machado'},
            #Catete
            {'parada_id': '2018O00026C0', 'estacao_nome': 'Catete'}, 
               #Glória
            {'parada_id': '2016O00030C0', 'estacao_nome': 'Glória'}, 
            {'parada_id': '2016O00032C0', 'estacao_nome': 'Glória'},
            #Carioca
            {'parada_id': '1005O00181C0', 'estacao_nome': 'Carioca'},
              {'parada_id': '1005O00236C0', 'estacao_nome': 'Carioca'}, 
              {'parada_id': '1005O00228C0', 'estacao_nome': 'Carioca'},
                 { 'parada_id': '1005O00227C0', 'estacao_nome': 'Carioca'},
                 { 'parada_id': '1005O00238S0', 'estacao_nome': 'Carioca'},
            #Uruguaiana
            { 'parada_id': '1005O00055S0', 'estacao_nome': 'Uruguaiana'},
            { 'parada_id': '1005O00046C2', 'estacao_nome': 'Uruguaiana'},
            { 'parada_id': '1005O00369C2', 'estacao_nome': 'Uruguaiana'},
             { 'parada_id': '1005O00142C0', 'estacao_nome': 'Uruguaiana'},
           { 'parada_id': '1005O00367C2', 'estacao_nome': 'Uruguaiana'},
           
            #Saara /  Presidente Vargas
           { 'parada_id': '1005O00170C0', 'estacao_nome': 'Saara/Presidente Vargas'},
            { 'parada_id': '1005O00158S0', 'estacao_nome': 'Saara/Presidente Vargas'},
            { 'parada_id': '1005O00026S9', 'estacao_nome': 'Saara/Presidente Vargas'},
           { 'parada_id': '1005O00376S2', 'estacao_nome': 'Saara/Presidente Vargas'} ,

           #Central
            { 'parada_id': '1005O00143C0', 'estacao_nome': 'Central'} ,
            { 'parada_id': '1005O00129P0', 'estacao_nome': 'Central'} ,
            {'parada_id': '1005O00377T9', 'estacao_nome': 'Central'} ,
            {'parada_id': '1005O00263P0', 'estacao_nome': 'Central'} ,
            {'parada_id': '1005O00005P0', 'estacao_nome': 'Central'} ,
            {'parada_id': '1005O00056S0', 'estacao_nome': 'Central'} ,
            {'parada_id': '1005O00027S0', 'estacao_nome': 'Central'} ,
            {'parada_id': '1005O00246S0', 'estacao_nome': 'Central'} ,
             {'parada_id': '1005O00033S0', 'estacao_nome': 'Central'} ,
            {'parada_id': '1005O00004S0', 'estacao_nome': 'Central'} ,
            {'parada_id': '1005O00025S0', 'estacao_nome': 'Central' }   ,   
            {'parada_id': '1005O00012S0', 'estacao_nome': 'Central' }  ,

            #Maracanã
            {'parada_id': '2035O00066C0', 'estacao_nome': 'Maracanã' }  ,
             {'parada_id': '2035O00080C0', 'estacao_nome': 'Maracanã' }  ,
            {'parada_id': '2033O00229C0', 'estacao_nome': 'Maracanã' }  ,
            {'parada_id': '2033O00214C0', 'estacao_nome': 'Maracanã' }  ,


            #Maria da Graça

            {'parada_id': '3052O00013C0', 'estacao_nome': 'Maria da Graça' },  
            {'parada_id': '3052O00020C0', 'estacao_nome': 'Maria da Graça' },   
            {'parada_id': '3052O00027C0', 'estacao_nome': 'Maria da Graça' } ,
            {'parada_id': '3052O00003C0', 'estacao_nome': 'Maria da Graça' } ,

            #Del Castiho

            {'parada_id': '3053O00025C0', 'estacao_nome': 'Del Castilho' }, 
            {'parada_id': '3053O00002C9', 'estacao_nome': 'Del Castilho' }, 
            {'parada_id': '3053O00027C0', 'estacao_nome': 'Del Castilho' }, 
            {'parada_id': '3053O00028C2', 'estacao_nome': 'Del Castilho' }, 
            {'parada_id': '3053O00020C9', 'estacao_nome': 'Del Castilho' },        
             
           #Uruguai
            { 'parada_id': '2033O00142C0', 'estacao_nome': 'Uruguai'},
             { 'parada_id': '2033O00173C0', 'estacao_nome': 'Uruguai'},

                      ]

        for parada in paradas:
            try:
                parada_obj = Parada.objects.get(parada_id=parada['parada_id'])
                parada_obj.integracao_metro = True
                parada_obj.estacao_metro = parada['estacao_nome']
                parada_obj.save()
            except Parada.DoesNotExist:
                self.stdout.write(self.style.ERROR(f'BusStop with parada_id {parada["parada_id"]} does not exist'))


