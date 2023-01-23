from gestionCliente.models import Clientes
from django.template import Template,Context
from django.template import loader
from django.http import HttpResponse
from django.shortcuts import render

def buscar2(request):
    doc_externo=loader.get_template('formulario3.html')
    
    ctx=Context()
    documento=doc_externo.render()
    return HttpResponse(documento)

def buscar3(request):
    id2=request.GET['id']
    art5=Clientes.objects.get(id=id2)
    art5.delete()
    doc_externo=loader.get_template('index.html')
    
    ctx=Context()
    documento=doc_externo.render()
    return HttpResponse(documento)