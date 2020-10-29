from main_app.views import prov_profile
from django.urls import path
from . import views

urlpatterns = [
    path('', views.home, name='home'),
    path('provider/<int:provider_id>', views.prov_profile, name='prov_profile'),
    path('dogs/', views.dogs_index, name='dogs'),
    path('registration/provider', views.provider_registration, name='prov_registration'),
    path('accounts/register_provider', views.register_provider, name='register_provider'),
]