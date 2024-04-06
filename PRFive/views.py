from django.shortcuts import render
from .models import Trainer

def index(request):
    return render(request, 'index.html')


def tovars(request):
    return render(request, 'tovar.html')


def trainers(request):
    all_trainers = Trainer.objects.all()
    return render(request, 'trainers.html', {'trainers': all_trainers})