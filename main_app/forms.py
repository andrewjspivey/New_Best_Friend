from django.forms import ModelForm
from django import forms
from django.contrib.auth.forms import UserCreationForm, ValidationError
from django.contrib.auth.models import User
from .models import Dog, Provider, User, RegUser
from django.db import transaction

class ProviderRegisterForm(UserCreationForm):
    shelterName = forms.CharField(max_length=75)
    location = forms.CharField(max_length=75)
    description = forms.CharField(max_length=500)
    phone = forms.CharField(max_length=15)
    website = forms.CharField(max_length=100)
    image = forms.CharField(max_length=200)
    adoptionProcess = forms.CharField(max_length=500)

    class Meta:
        model = User
        fields = ['username', 'email', 'password1', 'password2', 'shelterName',
            'location', 'description', 'phone', 'website', 'image', 'adoptionProcess']


    def save(self, commit=True):
        user = super(ProviderRegisterForm, self).save(commit=False)
        user.is_provider = True
        if commit:
            user.save()
        return user

class RegUserRegisterForm(UserCreationForm):
    image = forms.CharField(max_length=200)

    class Meta:
        model = User
        fields = ['first_name', 'last_name', 'username',
                'email', 'password1', 'password2', 'image']

    def save(self, commit=True):
        user = super(RegUserRegisterForm, self).save(commit=False)
        user.is_regUser = True
        if commit:
            user.save()
        return user


class Dog_Form(ModelForm):
    class Meta:
        model = Dog
        fields = ["name", "location", "breed", "age", "gender", "neutured",
            "image", "story"]


class EditProviderForm(ModelForm):
    shelterName = forms.CharField(max_length=75)
    location = forms.CharField(max_length=75)
    description = forms.CharField(max_length=500)
    phone = forms.CharField(max_length=15)
    website = forms.CharField(max_length=100)
    image = forms.CharField(max_length=200)
    adoptionProcess = forms.CharField(max_length=500)

    class Meta:
        model = User
        fields = ['username', 'email', 'shelterName', 'location', 
        'description', 'phone', 'website', 'image', 'adoptionProcess']

