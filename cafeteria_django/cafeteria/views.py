from django.shortcuts import render, redirect
from .form import ContactoForm
from .models import Barista

# Create your views here.

def home(request):
    return render(request,'cafeteria/home.html')

def menu(request):
    return render(request,'cafeteria/menu.html')

def baristas(request):
    personal = Barista.objects.all()
    return render(request,'cafeteria/baristas.html',{'personal' : personal})

def cafes(request):
    return render(request,'cafeteria/cafes.html')

def reseñas(request):
    return render(request,'cafeteria/reseñas.html')

def contacto(request):
    if request.method == 'POST':
        form = ContactoForm(request.POST)
        if form.is_valid():
            form.save()
            return redirect('home')
    else:
        form = ContactoForm    
    return render(request,'cafeteria/contacto.html',{'form':form})