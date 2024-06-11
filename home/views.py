from django.shortcuts import render
from django.db.models import Q, Max
import folium
import datetime 
from .models import LinhaDeOnibus,Viagem,Horario_Inicio, HorarioParada,Parada




def onibus_especifico(request,rota_numero): #condicao sppo =0, brt=1, frescao= 2

      linha = LinhaDeOnibus.objects.get(rota_numero=rota_numero) #selecionando a linha de onibus

      dia_atual =  datetime.datetime.now().weekday() #retorna formato numérico onde segunda feira é 0
      if  dia_atual >= 0 and dia_atual <= 5: #Segunda até Sexta
         q1 = Q( rota_numero=rota_numero , service='U_REG')
         q2 = Q(rota_numero=rota_numero ,service='U_OBRA_007')
         q3 = Q(rota_numero=rota_numero ,service='U_DESAT_OBRA_007')
         viagens = Viagem.objects.filter(q1 | q2 | q3)
      elif dia_atual == 6: #Sabado
         q1 = Q( rota_numero=rota_numero , service='S_REG')
         q2 = Q(rota_numero=rota_numero ,service='S_OBRA_007')
         q3 = Q(rota_numero=rota_numero ,service='S_OBRA_009')
         q4 = Q(rota_numero=rota_numero ,service='S_DESAT_OBRA_007')
         viagens = Viagem.objects.filter(q1 | q2 | q3| q4)
      else: #Domingo
         q1 = Q( rota_numero=rota_numero , service='D_REG')
         q2 = Q(rota_numero=rota_numero ,service='D_OBRA_007')
         q3 = Q(rota_numero=rota_numero ,service='D_OBRA_009')
         q4 = Q(rota_numero=rota_numero ,service='D_DESAT_OBRA_007')
         viagens = Viagem.objects.filter(q1 | q2 | q3 | q4  )

      viagens_id = [viagem.viagem_id for viagem in viagens] #pegando ids das viagem do dia selecionado
      horas = Horario_Inicio.objects.filter(viagem_id__in=viagens_id).values()
      tempo_de_espera_media = None
      if not horas:
         horas = HorarioParada.objects.filter(viagem_id__in=viagens_id, numero_parada = 0).values()
         horario1 = HorarioParada.objects.get(viagem_id=viagens_id[0], numero_parada= 0).horario
         horario2 = HorarioParada.objects.get(viagem_id=viagens_id[1], numero_parada= 0).horario
         diferenca = datetime.datetime.combine(datetime.date.today(), horario2) - datetime.datetime.combine(datetime.date.today(), horario1)
         diferenca = datetime.timedelta(minutes=30)
         tempo_de_espera_media = diferenca.total_seconds() // 60
         
         
      horas_dict = {horario['viagem_id']: horario['horario'] for horario in horas}
      
        
      viagens_com_horario = [] #criando lista que vai ser enviada para o html
      for viagem in viagens:
            viagem_dict = {
                'viagem_id': viagem.viagem_id,
                'destino_letreiro': viagem.destino_letreiro,
                'rota': viagem.rota,
                'rota_numero': viagem.rota_numero,
                'service': viagem.service,
                'horario': horas_dict.get(viagem.viagem_id, "")
            }
            viagens_com_horario.append(viagem_dict)
            viagens_com_horario = sorted(viagens_com_horario, key=lambda x: x['horario'])
      
      #eliminando viagens entre 00:00 e 03:59  em linhas padrão
      fim_do_dia = datetime.datetime.strptime('00:00:00', '%H:%M:%S').time()
      começo_do_dia = datetime.datetime.strptime('03:59:59', '%H:%M:%S').time()
      viagens_com_horario = [viagem for viagem in viagens_com_horario if not (fim_do_dia <= viagem['horario'] <= começo_do_dia)] # elimina todos que tem viagem  entre 00 e 03:59

      if tempo_de_espera_media is None:
          #calculando a média de tempo de espera 
         segundos = [l['tempo_intervalo'] for l in horas]
         media = sum(segundos)/ len(horas)
         tempo_de_espera_media = media/60
      
      
   
      #pegando a primeira e ultima parada.
      
      primeira_parada_id = HorarioParada.objects.get(viagem_id=viagens_id[0], numero_parada= 0).parada
      numero_ultimaparada = HorarioParada.objects.filter(viagem_id=viagens_id[0]).aggregate(Max('numero_parada'))['numero_parada__max']
      ultima_parada_id = HorarioParada.objects.get(viagem_id=viagens_id[0], numero_parada= numero_ultimaparada).parada
      nome_primeira_parada = Parada.objects.get(parada_id=primeira_parada_id).referencia_parada
      nome_ultima_parada = Parada.objects.get(parada_id=ultima_parada_id).referencia_parada

      parada_info= { 
         'primeira_parada':nome_primeira_parada,
          'ultima_parada': nome_ultima_parada,
          'total_paradas': str(numero_ultimaparada)}
      
      #pegar paradas no sentido 0
      id_viagem_destino0  = Viagem.objects.filter(viagem_id__in=viagens_id,destino_id=0).first().viagem_id
      paradas = HorarioParada.objects.filter(viagem_id=id_viagem_destino0)
      paradas_nome =[]
      cordenadas_das_paradas=[]

      for i in paradas:
         nome_parada = Parada.objects.filter(parada_id=i.parada).first().referencia_parada   
         paradas_nome.append(nome_parada)
         longitude = Parada.objects.filter(parada_id=i.parada).first().parada_longitude
         latitude = Parada.objects.filter(parada_id=i.parada).first().parada_latitude
         cordenadas_da_parada = (latitude,longitude)
         cordenadas_das_paradas.append(cordenadas_da_parada)

      origem =cordenadas_das_paradas[0]  # Exemplo de coordenadas da origem
      destino = cordenadas_das_paradas[-1] # Exemplo de coordenadas do destino
     
      mapa = folium.Map(location=origem, zoom_start=15)
      
     
      for ponto in cordenadas_das_paradas:
         latitude,longitude =ponto  
         folium.Marker(location=[latitude, longitude]).add_to(mapa)
         
      folium.Marker(location=cordenadas_das_paradas[0], popup='Localização Inicial', tooltip='Localização Inicial').add_to(mapa)
      folium.Marker(location=cordenadas_das_paradas[-1], popup='Localização Final', tooltip='Localização Final').add_to(mapa)
      coordenadas_linha = [(latitude, longitude) for latitude, longitude in cordenadas_das_paradas]

      folium.PolyLine(locations=coordenadas_linha, color='blue').add_to(mapa)

      map_html = mapa._repr_html_()   





      #verificando se é SPPO, BRT ou FRESCÃO
      condicao = verificar_linha(linha.rota_numero)

      contexto = {'viagens': viagens_com_horario, 'linha':linha,'map_html': map_html,'media_tempo': round(tempo_de_espera_media), 'condicao': condicao , 'parada_info':parada_info,'paradas':paradas,'paradas_nome':paradas_nome }
   
      return render(request, 'onibus_especifico.html',contexto)

def transporte_onibus (request):

   linhas = LinhaDeOnibus.objects.all().order_by('rota_numero')
   linhas_brt, linhas_frescao = listas_brt_frescao()

   contexto = {'linhas':linhas, 'linhas_brt': linhas_brt,'linhas_frescao': linhas_frescao}
   return render(request, 'transporte_onibus.html',contexto)

def transporte (request):
   return render(request, 'transporte.html')

def homepage(request):
   return render(request, 'homepage.html')

def verificar_linha (linha):
   linhas_brt , linhas_frescao = listas_brt_frescao()

   condicao = 0

   if linha in linhas_brt:
      condicao=1
   elif linha in linhas_frescao:
      condicao=2
   return int(condicao)


def listas_brt_frescao():
   linhas = LinhaDeOnibus.objects.all().order_by('rota_numero')
   linhas_brt=[]
   for linha in linhas:
      if len(linha.rota_numero) == 2 or linha.rota_numero == 'ESP01':
         linhas_brt.append(linha.rota_numero)
   
   linhas_frescao = []
   for linha in linhas:
      if len(linha.rota_numero) == 4 and linha.rota_numero[0]=='2':
         linhas_frescao.append(linha.rota_numero)
   
   return linhas_brt, linhas_frescao