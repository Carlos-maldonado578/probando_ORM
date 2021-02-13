from django.shortcuts import render, HttpResponse, redirect
from .models import Usuario
from django.contrib import messages

def index(request):
    return HttpResponse("Hola Mundooo")

def dev_usuarios(request):
    usuarios = Usuario.objects.all()
    context = {
        'usuarios': usuarios
    }
    return render(request, 'index.html', context)

def delete_usuario(request, id_usuario):
    consulta = Usuario.objects.get(id=id_usuario)
    consulta.delete()
    messages.error(request, 'Usuario Eliminado')
    return redirect('/usuarios')
# Create your views here.
