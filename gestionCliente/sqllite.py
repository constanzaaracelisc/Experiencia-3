from gestionCliente.models import Clientes
from django.template import Template,Context
from django.template import loader
from django.http import HttpResponse
from django.shortcuts import render

def Busqueda(request):
    doc_externo=loader.get_template('formulario.html')
    
    ctx=Context()
    documento=doc_externo.render()
    return HttpResponse(documento)
def buscar(request):
    nombres=request.GET['nom']
    dire=request.GET['dir']
    emai=request.GET['ema']
    tel=request.GET['tel']

    art=Clientes(Nombre=nombres,direccion=dire,email=emai,tele=tel)
    art.save()
    doc_externo=loader.get_template('index.html')
    
    ctx=Context()
    documento=doc_externo.render()
    return HttpResponse(documento)

