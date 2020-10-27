from django.db import models

# Create your models here.

class Dog(models.Model):
    name = models.CharField(max_length=50)
    location= models.CharField(max_length=50, null=True)
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
    image = models.CharField(max_length=200, default='photo.jpg')


