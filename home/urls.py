from django.urls import path
from . import views

app_name= 'home'

urlpatterns = [
    path('',views.homepage , name='homepage'),
   path('onibus/', views.onibus_especifico, name='onibus_especifico'),
]