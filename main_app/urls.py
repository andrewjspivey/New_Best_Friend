from main_app.views import prov_profile, dog_form, add_dog
from django.urls import path
from . import views

urlpatterns = [
    path('', views.home, name='home'),
    path('provider/<int:provider_id>/', views.prov_profile, name='prov_profile'),
    path('provider/<int:provider_id>/dog_add', views.add_dog, name='add_dog'),
    path('provider/<int:provider_id>/dog_form/', views.dog_form, name='dog_form'),
    path('dogs/', views.dogs_index, name='dogs'),
    path('dogs/<int:dog_id>/edit', views.edit_dog, name='edit_dog'),
    path('registration/', views.registration_type, name='registration'),
    path('registration/provider/', views.provider_registration, name='prov_registration'),
    path('registration/regUser/', views.regUser_registration, name='regUser_registration'),
    path('accounts/register/provider', views.register_provider, name='register_provider'),
    path('accounts/register/regUser', views.register_regUser, name='register_regUser'),
]