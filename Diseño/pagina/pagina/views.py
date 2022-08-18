from django.shortcuts import render

def pagina(request):
    return  render (request, 'pagina.html')

def acercadenosotros(request):
    return  render (request, 'acercadenosotros.html')

def login(request):
    return  render (request, 'login.html')