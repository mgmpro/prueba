from django.urls import path

from . import views

urlpatterns = [
    path('ejercicios',views.ejercicios, name="Ejercicios"),
    path('calculos',views.calculos, name="Calculos"),
    path('terminos',views.terminos, name="Terminos"),
    path('adivinanzas',views.adivinanzas, name="Adivinanzas"),
    path('cultura',views.cultura, name="Cultura"),
    path('historia',views.historia, name="Historia"),
    path('capitales',views.capitales, name="Capitales"),

]

