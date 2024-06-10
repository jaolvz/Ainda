from django.shortcuts import render, redirect
from django.db.models import Q
import datetime
from .models import LinhaDeOnibus,Viagem,Horario_Inicio, HorarioParada


def onibus_especifico(request):
   if request.method == 'POST':

      

      onibus_selecionado = request.POST.get('onibus_selecionado')
      linha = LinhaDeOnibus.objects.get(rota_numero=onibus_selecionado) #selecionando a linha de onibus

      dia_atual = datetime.datetime.now().weekday() #retorna formato numérico onde segunda feira é 0
      if  dia_atual >= 0 and dia_atual <= 5: #Segunda até Sexta
         q1 = Q( rota_numero=onibus_selecionado , service='U_REG')
         q2 = Q(rota_numero=onibus_selecionado ,service='U_OBRA_007')
         viagens = Viagem.objects.filter(q1 | q2)
      elif dia_atual == 6: #Sabado
         q1 = Q( rota_numero=onibus_selecionado , service='S_REG')
         q2 = Q(rota_numero=onibus_selecionado ,service='S_OBRA_007')
         q3 = Q(rota_numero=onibus_selecionado ,service='S_OBRA_009')
         viagens = Viagem.objects.filter(q1 | q2 | q3)
      else: #Domingo
         q1 = Q( rota_numero=onibus_selecionado , service='D_REG')
         q2 = Q(rota_numero=onibus_selecionado ,service='D_OBRA_007')
         q3 = Q(rota_numero=onibus_selecionado ,service='D_OBRA_009')
         viagens = Viagem.objects.filter(q1 | q2 | q3)
      viagens_id = [viagem.viagem_id for viagem in viagens] #pegando ids das viagem do dia selecionado
      horas = Horario_Inicio.objects.filter(viagem_id__in=viagens_id).values()
      if not horas:
         horas = HorarioParada.objects.filter(viagem_id__in=viagens_id, numero_parada = 0).values()
  
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
      contexto = {'linha':linha, 'viagens':viagens_com_horario}
      

      return render(request, 'onibus_especifico.html',contexto)



def homepage(request):
   linhas = LinhaDeOnibus.objects.all().order_by('rota_numero')
   contexto = {'linhas':linhas}
   return render(request, 'homepage.html',contexto)