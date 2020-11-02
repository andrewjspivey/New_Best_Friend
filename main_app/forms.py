from django.forms import ModelForm
from django import forms
from django.contrib.auth.forms import UserCreationForm, ValidationError
from django.contrib.auth.models import User
from .models import Dog, Provider, User, RegUser
from django.db import transaction

class ProviderRegisterForm(UserCreationForm):
    shelterName = forms.CharField(widget=forms.TextInput(attrs={'class' : 'form-control'}))
    location = forms.CharField(widget=forms.TextInput(attrs={'class' : 'form-control'}))
    phone = forms.CharField(widget=forms.TextInput(attrs={'class' : 'form-control'}))
    website = forms.CharField(widget=forms.TextInput(attrs={'class' : 'form-control'}))
    image = forms.CharField(widget=forms.TextInput(attrs={'class' : 'form-control'}))
    description = forms.CharField(widget=forms.Textarea(attrs={'class' : 'form-control'}))
    adoptionProcess = forms.CharField(widget=forms.Textarea(attrs={'class' : 'form-control'})) 

    class Meta:
        model = User
        fields = ['username', 'email', 'password1', 'password2', 'shelterName',
            'location', 'phone', 'website', 'image', 'description', 'adoptionProcess']


    def save(self, commit=True):
        user = super(ProviderRegisterForm, self).save(commit=False)
        user.is_provider = True
        if commit:
            user.save()
        return user

    def __init__(self, *args, **kwargs):
        super(ProviderRegisterForm, self).__init__(*args, **kwargs)

        self.fields['username'].widget.attrs['class'] = 'form-control'
        self.fields['email'].widget.attrs['class'] = 'form-control'
        self.fields['password1'].widget.attrs['class'] = 'form-control'
        self.fields['password2'].widget.attrs['class'] = 'form-control'

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

