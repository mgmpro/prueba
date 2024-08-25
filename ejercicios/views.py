from django.shortcuts import render

# Create your views here.

def ejercicios(request):

    return render(request, "ejercicios/ejercicios.html")

def calculos(request):

    return render(request, "ejercicios/calculos.html")

def terminos(request):

    return render(request, "ejercicios/terminos.html")

def adivinanzas(request):

    return render(request, "ejercicios/adivinanzas.html")

def cultura(request):

    return render(request, "ejercicios/cultura.html")

def historia(request):

    return render(request, "ejercicios/historia.html")

def capitales(request):

    return render(request, "ejercicios/capitales.html")


