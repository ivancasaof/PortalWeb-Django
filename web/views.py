from cgitb import text
from tkinter.messagebox import NO
from django.shortcuts import redirect, render, get_list_or_404, get_object_or_404
from .models import Noticias

def index(request):
    noticias_geral = Noticias.objects.order_by('-data')
    noticias_comunicado = Noticias.objects.order_by('-data').filter(categoria=1)
    noticias_evento = Noticias.objects.order_by('-data').filter(categoria=2)

    noticias_rh_comunicados = Noticias.objects.order_by('-data').filter(categoria=4)

    dados ={
        'noticias_comunicado' : noticias_comunicado,
        'noticias_evento' : noticias_evento,
        'noticias_rh_comunicados' : noticias_rh_comunicados,
        'noticias_geral' : noticias_geral,
        
    }
    return render(request, 'index.html', dados)

def noticias_geral(request, noticias_id):
    obj = get_object_or_404(Noticias, pk=noticias_id)
    noticia_a_exibir = {
        'noticia' : obj
    }
    categoria = str(obj.categoria)
    if categoria == "RH Comunicados":
        return render(request, 'rh_comunicados_ativo.html', noticia_a_exibir)
    elif categoria == "Eventos":
        return render(request, 'eventos_ativo.html', noticia_a_exibir)
    elif categoria == "Comunicados":
        print('asd')
        return render(request, 'comunicados_ativo.html', noticia_a_exibir)
    

def comunicados(request):
    noticias = Noticias.objects.order_by('-data').filter(categoria_id=1)
    ultima_noticia = Noticias.objects.last()

    dados ={
        'noticia' : noticias,
        'ultima_noticia' : ultima_noticia
    }

    return render(request, 'comunicados.html', dados)

def comunicados_ativo(request, noticia_id):
    noticias = get_object_or_404(Noticias, pk=noticia_id)

    noticia_a_exibir = {
        'noticia' : noticias
    }

    return render(request,'comunicados_ativo.html', noticia_a_exibir)

def eventos(request):
    noticias_evento = Noticias.objects.order_by('-data').filter(categoria_id=2)

    dados ={
        'noticias_evento' : noticias_evento,
    }

    return render(request, 'eventos.html', dados)

def eventos_ativo(request, evento_id):
    noticia_evento = get_object_or_404(Noticias, pk=evento_id)

    noticia_a_exibir = {
        'noticia' : noticia_evento
    }

    return render(request,'eventos_ativo.html', noticia_a_exibir)

def rh_comunicados(request):
    noticias_rh_comunicados = Noticias.objects.order_by('-data').filter(categoria=4)

    dados ={
        'noticia' : noticias_rh_comunicados,
    }

    return render(request, 'rh_comunicados.html', dados)


def rh_comunicados_ativo(request, rh_comunicados_id):
    noticias_rh_comunicados = get_object_or_404(Noticias, pk=rh_comunicados_id)

    dados ={
        'noticia' : noticias_rh_comunicados,
    }

    return render(request, 'rh_comunicados_ativo.html', dados)

def empresa(request):
    return render(request, 'empresa.html')
