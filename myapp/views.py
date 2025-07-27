from django.shortcuts import render
from django.contrib.auth.models import User
from django.http import JsonResponse
from .models import CentroComercial, Tienda

# Create your views here.
def lista_centros_comerciales(request):
    centros_comerciales = CentroComercial.objects.all()
    return render(request, 'lista_centros_comerciales.html', {'centros_comerciales': centros_comerciales})

def lista_tiendas(request):
    tiendas = Tienda.objects.all()
    return render(request, 'lista_tiendas.html', {'tiendas': tiendas})

def vista_centro_comercial(request, name_cc):
    centro_comercial = CentroComercial.objects.get(nombre=name_cc)
    tiendas = centro_comercial.tiendas.all()
    return render(request, 'vista_centro_comercial.html', {'centro_comercial': centro_comercial, 'tiendas': tiendas})

def profile_view(request):
    if request.method == 'POST':
        data = request.POST
        new_first_name = data['first_name']
        new_last_name = data['last_name']
        user_id = request.user.id
        
        user = User.objects.get(id=user_id)
        user.first_name = new_first_name
        user.last_name = new_last_name
        user.save()
        return JsonResponse({'status': 'success'})
    
    return render(request, 'profile.html')