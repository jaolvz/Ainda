from django.urls import path
from . import views

app_name= 'home'

urlpatterns = [
    path('',views.homepage , name='homepage'),
  
   path('transporte/', views.transporte, name='transporte'),
    path('transporte/onibus', views.transporte_onibus, name='transporte_onibus'),
     path('transporte/onibus/<str:rota_numero>', views.onibus_especifico, name='onibus_especifico'),
   
]