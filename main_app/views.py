from django.shortcuts import render
from .models import Dog
# Create your views here.


def home(request):
    return render(request, "home.html")


def dogs_index(request):
    dogs = Dog.objects.all()
    context = {"dogs": dogs}

    return render(request, "dogs/index.html", context)