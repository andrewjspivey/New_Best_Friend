from django.db import models
from django.contrib.auth.models import AbstractUser
from django.urls import reverse
from datetime import datetime
from django.db.models.signals import post_save
from django.dispatch import receiver
from django.utils import timezone
# Create your models here.


class User(AbstractUser):
    is_provider = models.BooleanField(default=False)
    is_regUser = models.BooleanField(default=False)



class Provider(models.Model):
    user = models.OneToOneField(User, on_delete=models.CASCADE)
    user.is_provider = True
    shelterName = models.CharField(max_length=75)
    location = models.CharField(max_length=75)
    description = models.TextField(max_length=500, null=True)
    phone = models.CharField(max_length=15, null=True)
    website = models.CharField(max_length=100, null=True)
    image = models.CharField(max_length=200, null=True)
    adoptionProcess = models.TextField(max_length=500, null=True)

    def __str__(self):
        return self.shelterName


class RegUser(models.Model):
    user = models.OneToOneField(User, on_delete=models.CASCADE)
    user.is_regUser = True
    image = models.CharField(max_length=200, null=True)
    

    def __str__(self):
        return self.user.username


@receiver(post_save, sender=User)
def create_user_profile(sender, instance, created, **kwargs):
    if created:
        if instance.is_provider:
            Provider.objects.get_or_create(user=instance)
        elif instance.is_regUser:
            RegUser.objects.get_or_create(user=instance) 

@receiver(post_save, sender=User)
def save_user_profile(sender, instance, **kwargs):
    if instance.is_provider:
        instance.provider.save()
    elif instance.is_regUser:
        instance.reguser.save()


class Dog(models.Model):
    name = models.CharField(max_length=50)
    location= models.CharField(max_length=50)
    breed = models.CharField(max_length=50)
    age = models.CharField(max_length=50)
    DOG_GENDER = (
        ("M", "Male"),
        ("F", "Female"),
    )
    IS_NEUTURED = (
        ("Y", "Yes"),
        ("N", "No"),
        ("U", "Unknown")
    )
    gender = models.CharField(max_length=1, choices=DOG_GENDER, null=True)
    neutured = models.CharField(max_length=1, choices=IS_NEUTURED, null=True)
    image = models.CharField(max_length=200, default="photo.jpg")
    story = models.TextField(max_length=700, default="story")
    provider = models.ForeignKey(Provider, on_delete=models.CASCADE)


    def __str__(self):
        return self.name


