from main_app.views import dog_form, add_dog, pf_dog_show
from django.urls import path, include
from . import views


urlpatterns = [
    path('search/', views.search_results, name='search_results'),
    path('', views.home, name='home'),
    path('pf_orgs/', views.orgs_index, name='orgs_index'),
    path('v2/organizations/<str:org_id>/', views.orgs_show, name='orgs_show'),
    path('provider/<int:provider_id>/', views.prov_profile, name='prov_profile'),
    path('provider/<int:provider_id>/dog_add', views.add_dog, name='add_dog'),
    path('provider/<int:provider_id>/dog_form/', views.dog_form, name='dog_form'),
    path('provider/<int:provider_id>/edit_provider/', views.edit_provider, name='edit_provider'),
    path('provider/<int:provider_id>/edit_form/', views.edit_provider_form, name='edit_provider_form'),
    path('shelters/', views.shelter_index, name='shelter_index'),
    path('dogs/', views.dogs_index, name='dogs'),
    path('dogs/<int:dog_id>/', views.dog_show, name='dog_show'),
    path('pfdogs/<int:dog_id>/', views.pf_dog_show, name='pf_dog_show'),
    path('dogs/<int:dog_id>/edit', views.edit_dog, name='edit_dog'),
    path('dogs/<int:dog_id>/delete', views.delete_dog, name='delete_dog'),
    path('registration/', views.registration_type, name='registration'),
    path('registration/provider/', views.provider_registration, name='prov_registration'),
    path('registration/regUser/', views.regUser_registration, name='regUser_registration'),
    path('accounts/register/provider', views.register_provider, name='register_provider'),
    path('accounts/register/regUser', views.register_regUser, name='register_regUser'),
]