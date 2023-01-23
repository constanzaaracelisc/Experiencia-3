from django.template import Template,Context
from django.http import HttpResponse
from django.template import loader

def saludo(request):
    #adoc_externo=open('')
    #plt=Template(doc_externo.read())
    #doc_externo.close()
    doc_externo=loader.get_template('index.html')
    
    ctx=Context()
    documento=doc_externo.render()
    return HttpResponse(documento)


def quienes(request):
    doc_externo=loader.get_template('quienes.html')
    
    ctx=Context()
    documento=doc_externo.render()
    return HttpResponse(documento)
    
def contacto(request):
    doc_externo=loader.get_template('contacto.html')
    
    ctx=Context()
    documento=doc_externo.render()
    return HttpResponse(documento)

def galeria(request):
    doc_externo=loader.get_template('galeria.html')
    
    ctx=Context()
    documento=doc_externo.render()
    return HttpResponse(documento)


