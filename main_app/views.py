from django.shortcuts import render
from .models import Dog, Provider
# Create your views here.


def home(request):
    return render(request, "home.html")


def dogs_index(request):
    dogs = Dog.objects.all()
    context = {"dogs": dogs}

    return render(request, "dogs/index.html", context)


def prov_profile(request, provider_id):
    provider = Provider.objects.get(id=provider_id)
    context = {
        'provider': provider,
    }
    return render(request, 'profile/prov_profile.html', context)