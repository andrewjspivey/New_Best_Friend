
import os
import requests
import petpy
import dotenv
from NewBestFriend_project.settings import API_KEY, SECRET
import environ

pf = petpy.Petfinder(key=API_KEY, secret=SECRET)


def get_dogs():
    url = 'https://api.petfinder.com/v2/animals?type=dog&limit=50'

    dogs = pf.animals(animal_type='dog', results_per_page=20, pages=2, location='San Francisco, CA')

    all_dogs = []

    for i in dogs['animals'][0:50]:
        all_dogs.append(i)
    ## animal_data = pf.animals(animal_names=animal_names)
    ##animals = pf.animals(results_per_page=15, pages=1, return_df=True)
    return all_dogs


def get_orginizations():
    orgs = pf.organizations(location="San Francisco, CA")

    all_orgs = []

    for i in orgs['organizations'][0:20]:
        all_orgs.append(i)

    return all_orgs
