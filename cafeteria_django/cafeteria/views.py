from django.shortcuts import render

# Create your views here.

def home(request):
    return render(request,'cafeteria/home.html')

def menu(request):
    return render(request,'cafeteria/menu.html')

def baristas(request):
    return render(request,'cafeteria/baristas.html')

def cafes(request):
    return render(request,'cafeteria/cafes.html')

def reseñas(request):
    return render(request,'cafeteria/reseñas.html')

def contacto(request):
    return render(request,'cafeteria/contacto.html')