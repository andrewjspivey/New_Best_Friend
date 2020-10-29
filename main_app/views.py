from django.shortcuts import render, redirect
from .models import Dog, Provider, User, RegUser
from django.contrib.auth.models import AbstractUser
from django.contrib.auth.forms import UserCreationForm
from .forms import ProviderRegisterForm, Dog_Form
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

def provider_registration(request):
    form = ProviderRegisterForm()
    context = {
        'form': form,
    }
    return render(request, 'registration/register_provider.html',  context)

def register_provider(request):
    if request.method == 'POST':
        form = ProviderRegisterForm(request.POST)
        if form.is_valid():
            user = form.save()
            user.is_provider = True
            user.provider.shelterName = form.cleaned_data.get('shelterName')
            user.provider.location = form.cleaned_data.get('location')
            user.provider.description = form.cleaned_data.get('description')
            user.provider.phone = form.cleaned_data.get('phone')
            user.provider.website = form.cleaned_data.get('website')
            user.provider.image = form.cleaned_data.get('image')
            user.provider.adoptionProcess = form.cleaned_data.get('adoptionProcess')
            user.save()
            return redirect("home") 
        else:
            form = ProviderRegisterForm()

        return render(request, 'home', {'form': form})
        