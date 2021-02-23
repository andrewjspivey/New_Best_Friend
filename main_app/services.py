
import os
import requests
import petpy
import dotenv
from NewBestFriend_project.settings import API_KEY, SECRET
import environ



pf = petpy.Petfinder(key=API_KEY, secret=SECRET)

def get_dogs():
    url = 'https://api.petfinder.com/v2/animals?type=dog&limit=50'

    dogs = pf.animals(animal_type='dog', results_per_page=25, pages=2, location='San Francisco, CA')

    all_dogs = []

    for i in dogs['animals'][0:60]:
        all_dogs.append(i)

    return all_dogs


def get_orginizations():
    orgs = pf.organizations(location="San Francisco, CA")

    all_orgs = []

    for i in orgs['organizations'][0:20]:
        all_orgs.append(i)

    return all_orgs

