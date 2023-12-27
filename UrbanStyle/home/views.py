from django.shortcuts import redirect, render
from django.http import HttpResponse


def welcomeMessage(request):
    return HttpResponse("<h1> Esta es la página de inicio de la app<h1>")

def showMessage(request, name:str):
    return HttpResponse("Mensaje desde views. Hola %s" % name)

def toHome(request):
    return redirect("home")