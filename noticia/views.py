from django.shortcuts import render
from .models import Registro
from .forms import RegistroForm

# Create your views here.
def index(request):
    return render(request, 'index.html')

def mostrar(request):
    registro=Registro.objects.all()
    return render(request, 'noticia/mostrar.html', context={'every':registro})

def form_agreg(request):
    if request.method=='GET':
        formulario=RegistroForm()
        contexto={
            'formulario':formulario
        }
    else:
        formulario=RegistroForm(request.POST)
        contexto={
            'formulario':formulario
        }
        if formulario.is_valid:
            formulario.save()
            return redirect('mostrar')

    return render(request, 'noticia/form_agreg.html', {'formulario':formulario})

def form_mod(request,id):
    registro = Registro.objects.get(rut=id)

    datos ={
        'form': RegistroForm(instance=registro)
    }
    if request.method == 'POST': 
        formulario = RegistroForm(data=request.POST, instance = registro)
        if formulario.is_valid: 
            formulario.save()           #permite actualizar la info del objeto encontrado
            return redirect('mostrar')
    return render(request, 'noticia/form_mod.html', datos)

def form_del(request,id):
    registro = Registro.objects.get(rut=id)
    registro.delete()
    return redirect('mostar')


