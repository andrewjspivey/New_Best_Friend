from django.shortcuts import render, redirect
from .models import Dog, Provider, User, RegUser
from django.contrib.auth.models import AbstractUser
from django.contrib.auth.forms import UserCreationForm
from .forms import ProviderRegisterForm, RegUserRegisterForm, Dog_Form
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

def registration_type(request):
    return render(request, 'registration/register.html')

def provider_registration(request):
    form = ProviderRegisterForm()
    context = {
        'form': form,
    }
    return render(request, 'registration/register_provider.html',  context)


def regUser_registration(request):
    form = RegUserRegisterForm()
    context = {
        'form': form,
    }
    return render(request, 'registration/register_regUser.html',  context)

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


def register_regUser(request):
    if request.method == 'POST':
        form = RegUserRegisterForm(request.POST)
        if form.is_valid():
            user = form.save()
            user.is_regUser = True
            user.reguser.image = form.cleaned_data.get('image')
            user.save()
            return redirect("home") 
        else:
            form = RegUserRegisterForm()

        return render(request, 'home', {'form': form})


def add_dog(request, provider_id):
    provider = Provider.objects.get(id=provider_id)
    if request.method == 'POST':
        dog_form = Dog_Form(request.POST)
        if dog_form.is_valid():
            new_dog = dog_form.save(commit=False)
            new_dog.provider = provider
            new_dog.save()
        return redirect('home')


def dog_form(request, provider_id):
    provider = Provider.objects.get(id=provider_id)
    form = Dog_Form()
    context = {
        "provider": provider,
        "form": form,
    }
    return render(request, "dogs/dog_form.html", context)

    
    


        
