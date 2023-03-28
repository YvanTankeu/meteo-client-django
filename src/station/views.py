from django.shortcuts import render
from .models import Donnees

def donnees(request):
    donnees = Donnees.objects.all()
    return render(request, 'donnees.html', {'donnees': donnees})
