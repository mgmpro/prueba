from django.shortcuts import render, HttpResponse 


# Create your views here.

def home(request):

    return render(request, "SistemaEjerciciosApp/home.html")

def nosotros(request):

    return render(request, "SistemaEjerciciosApp/nosotros.html")







