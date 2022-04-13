from django.shortcuts import render, redirect
from .models import Apartamento, Switche, Patchera
from .forms import ApartamentForm

def apartamento(request):
    queryset = Apartamento.objects.all()
    context={
        "queryset":queryset,
        
    }
    
    return render(request, 'index.html', context)

def Building(request) :
    if request.method == "POST" :
        apartament_form = ApartamentForm(request.POST)
        if apartament_form.is_valid() :
            apartament_form.save()
            return redirect('index')
    else :
        apartament_form = ApartamentForm()

    return render(
        request , 'agregar.html' ,
        {
            'apartament_form' : apartament_form
        }
    )
    
#******************************************************************************
def Apartamentos(request):
    apartamentos = Apartamento.objects.all()
    context={
        "apartamentos":apartamentos,
    }
    return render(request, 'apartamentos.html', context)


def Switches(request):
    switches = Switche.objects.all()
    context={
        "switches":switches,
        
    }
    
    return render(request, 'switches.html', context)

def Patcheras(request):
    patcheras = Patchera.objects.all()
    context={
        "patcheras":patcheras,
        
    }
    
    return render(request, 'patcheras.html', context)