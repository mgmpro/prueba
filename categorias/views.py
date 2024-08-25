from django.shortcuts import render
from categorias.models import Categoria

# Create your views here.

def ofrecemos(request):

    categorias=Categoria.objects.all()
    return render(request, "categorias/ofrecemos.html", {"categorias": categorias})
