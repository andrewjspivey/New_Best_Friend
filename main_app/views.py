from django.shortcuts import render, redirect
from django.contrib.auth.models import AbstractUser
from django.contrib.auth.forms import UserCreationForm
from django.db.models import Q
from django.contrib.auth import login, authenticate
from django.views.generic import ListView
from django.http import JsonResponse
from django.contrib import messages

from .models import Dog, Provider, User, RegUser
from .forms import ProviderRegisterForm, RegUserRegisterForm, Dog_Form, EditProviderForm
from main_app.services import get_dogs, get_orginizations
import petpy
import requests
import dotenv
from NewBestFriend_project.settings import API_KEY, SECRET
import environ
import os


pf = petpy.Petfinder(key=API_KEY, secret=SECRET)

def home(request):
    signup_modal = RegUserRegisterForm()

    dogs = pf.animals(animal_type='dog', location="San Francisco, CA", results_per_page=11)
    dogs_list = []
    for dog in dogs['animals']:
        dogs_list.append(dog)
    context = {
        "signup_modal": signup_modal,
        "dogs_list": dogs_list,
    }
    return render(request, "home.html", context)



def search_results(request):

    try:
        query = request.GET.get('q')
        dogs = pf.animals(animal_type='dog',location=query, distance=20, results_per_page=40)
        dogs_list = []
        for dog in dogs['animals']:
            dogs_list.append(dog)

        context = {
            "dogs_list": dogs_list,
        }
        return render(request, "search_results.html", context)
    except petpy.exceptions.PetfinderInvalidParameters:
        messages.info(request, "You must search in this format: City, State(CA|NY) or postal code")
        return redirect('dogs')






def dogs_index(request):
    signup_modal = RegUserRegisterForm()
    context = {
        "dogs": get_dogs(),
        "signup_modal": signup_modal,
    }

    return render(request, "dogs/index.html", context)


def dog_show(request, dog_id):
    dog = Dog.objects.get(id=dog_id)
    provider = Provider.objects.all()
    signup_modal = RegUserRegisterForm()
    context = {
        "dog": dog,
        "provider": provider,
        "signup_modal": signup_modal,
    }
    return render(request, "dogs/show.html", context)

## DONT FORGET TO INCLUDE SEARCH FOR PF DOGS!

def pf_dog_show(request, dog_id):
    dog = pf.animals(animal_id=dog_id)
    signup_modal = RegUserRegisterForm()
    context = {
        "dog": dog,
        "signup_modal": signup_modal,
    }
    return render(request, "dogs/pf_show.html", context)

def shelter_index(request):
    providers = Provider.objects.all()
    context = {
        "providers": providers,
    }
    return render(request, "shelter/index.html", context)


def orgs_index(request):
    context = {
        "orgs": get_orginizations(),
    }
    return render(request, "shelter/pf_orgs.html", context)


def orgs_show(request, org_id):
    org = pf.organizations(organization_id=org_id,)
    dogs = pf.animals(organization_id=org_id, animal_type="dog")
    context = {
        'org': org,
        'dogs': dogs,
    }
    return render(request, 'profile/org_show.html', context)


def prov_profile(request, provider_id):
    provider = Provider.objects.get(id=provider_id)
    dogs = Dog.objects.all()
    context = {
        'provider': provider,
        'dogs': dogs,
    }
    return render(request, 'profile/prov_profile.html', context)


def edit_provider(request, provider_id):
    provider = Provider.objects.get(id=provider_id)
    if request.method == 'POST':
        edit_form = EditProviderForm(request.POST, instance=provider)
        if edit_form.is_valid():
            edit_form.save()
            return redirect('home')
    else:
        edit_form = EditProviderForm()
        context = {
            'provider': provider,
            'edit_form': edit_form
        }
        return render(request, 'profile/edit.html', context)


def edit_provider_form(request, provider_id):
    provider = Provider.objects.get(id=provider_id)
    if (provider.id == request.user.provider.id):
        edit_form = EditProviderForm(initial={
            'shelterName': provider.shelterName,
            'location': provider.location,
            'description': provider.description,
            'phone': provider.phone,
            'website': provider.website,
            'image': provider.image,
            'adoptionProcess': provider.adoptionProcess,
        })
        context = {
            "provider": provider,
            "edit_form": edit_form,
        }
        return render(request, "profile/profile_editform.html", context)
    elif (request.user.is_regUser):
        return redirect("login")




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
    error_message = ''
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
            login(request, user)
            return redirect("home") 
        else:
            error_message = 'Please try again and make sure your passwords are the same and email is valid'
    form = ProviderRegisterForm()
    context = {'form': form, 'error_message': error_message}
    return render(request, 'registration/register_provider.html', context)

def register_regUser(request):
    error_message = ''
    if request.method == 'POST':
        form = RegUserRegisterForm(request.POST)
        if form.is_valid():
            user = form.save()
            user.is_regUser = True
            user.reguser.image = form.cleaned_data.get('image')
            user.save()
            login(request, user)
            return redirect("home") 
        else:
            error_message = 'Please try again with matching passwords and a valid email'
    form = RegUserRegisterForm()
    context = {'form': form, 'error_message': error_message}
    return render(request, 'registration/register_regUser.html', context)


def add_dog(request, provider_id):
    error_message = ''
    provider = Provider.objects.get(id=provider_id)
    if request.method == 'POST':
        dog_form = Dog_Form(request.POST)
        if dog_form.is_valid():
            new_dog = dog_form.save(commit=False)
            new_dog.provider = provider
            new_dog.save()
            return redirect('prov_profile', provider.id)
        else:
            error_message = 'Please try again, make sure the form is complete and the image is a link'
    dog_form = Dog_Form()
    context = {'dog_form': dog_form, 'error_message': error_message}
    return render(request, 'dogs/dog_form.html', context)


def dog_form(request, provider_id):
    provider = Provider.objects.get(id=provider_id)
    form = Dog_Form()
    context = {
        "provider": provider,
        "form": form,
    }
    return render(request, "dogs/dog_form.html", context)

    
def edit_dog(request, dog_id):
    dog = Dog.objects.get(id=dog_id)
    if (dog.provider.id == request.user.provider.id):
        if request.method == 'POST':
            edit_form = Dog_Form(request.POST, instance=dog)
            if edit_form.is_valid():
                edit_form.save()
                return redirect('home')
        else:
            edit_form = Dog_Form(initial={
                'name': dog.name,
                'location': dog.location,
                'breed': dog.breed,
                'age': dog.age,
                'gender': dog.gender,
                'neutured': dog.neutured,
                'image': dog.image,
                'story': dog.story,
            })
            context = {
                'dog': dog,
                'edit_form': edit_form
            }
            return render(request, 'dogs/edit.html', context)
    else:
        return redirect('home')
    

def delete_dog(request, dog_id):
    Dog.objects.get(id=dog_id).delete()
    return redirect('prov_profile', request.user.provider.id)
        

