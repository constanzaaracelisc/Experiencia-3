from gestionCliente.models import Clientes
from django.template import Template,Context
from django.template import loader
from django.http import HttpResponse
from django.shortcuts import render
import sqlite3


def mostrar(request):
    doc_externo=loader.get_template('indice.html')
    conn=sqlite3.connect('db.sqlite3')
    cursor=conn.execute('select* from gestionCliente_clientes')
    filas=cursor.fetchall()
    temas=[]
    for fila in filas:
        temas.append(fila)
    conn.commit()
    conn.close()
        
    documento=doc_externo.render({"temas":temas})    
   
    return HttpResponse(documento)
    
    