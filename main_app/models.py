from django.db import models

# Create your models here.



class Provider(models.Model):
    name = models.CharField(max_length=75)
    location = models.CharField(max_length=75)
    description = models.TextField(max_length=500)
    phone = models.CharField(max_length=15)
    website = models.CharField(max_length=100)
    image = models.CharField(max_length=200)
    adoptionProcess = models.TextField(max_length=500)

    def __str__(self):
        return self.name

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
    image = models.CharField(max_length=200, default="photo.jpg")
    story = models.TextField(max_length=700, default="story")
    provider = models.ForeignKey(Provider, on_delete=models.CASCADE, default="none")

    def __str__(self):
        return self.name


