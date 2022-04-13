from django.urls import path
from .views import apartamento, Switches, Patcheras, Apartamentos, Building

urlpatterns = [
    path('', apartamento, name = 'index'),
    path('switches', Switches,  name = 'switch'),
    path('patcheras', Patcheras,  name = 'patch'),
    path('apartamentos', Apartamentos,  name = 'apartment'),
    path('agregar', Building,  name = 'agregar'),

]