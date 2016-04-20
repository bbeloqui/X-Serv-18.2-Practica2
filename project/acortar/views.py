from django.shortcuts import render
from django.http import HttpResponseRedirect, HttpResponseNotFound, HttpResponse
from models import Url
from django.views.decorators.csrf import csrf_exempt

# Create your views here.

def acortador(request, fila):
    try:
        urls = Url.objects.get(id=fila)
        return HttpResponseRedirect(urls.original)
    except Url.DoesNotExist:
        return HttpResponseNotFound('Esa url acortada no existe')
    except ValueError:
        return HttpResponseNotFound('Esa url acortada no existe')

@csrf_exempt
def general(request):
    formulario =""

    if request.method == "GET":
        datos = Url.objects.all()
        for fila in datos:
            formulario += "<p><a href="'/'+ str(fila.id) +'>'+ "localhost:8000/"+str(fila.id) +'</a>'+ " corresponde a " + fila.original + " " +'</p>'

    if request.method == "POST":
        url = request.POST["nombre"]
        if not(url.startswith('http')):
            url= 'http://' + url
        try:
            fila = Url.objects.get(original=url)
            formulario += "<p>La url que esta intentando acortar ya esta acortada</p>"
        except Url.DoesNotExist:
            fila = Url(original=url)
            fila.save()
        datos = Url.objects.all()
        for fila in datos:
            formulario += "<p><a href="'/'+ str(fila.id) +'>'+ "localhost:8000/"+str(fila.id) +'</a>'+ " corresponde a " + fila.original + " " +'</p>'

    context = {'contenido': formulario}
    return render(request, 'practica2.html', {'context': context})
