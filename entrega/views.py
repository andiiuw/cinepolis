from django.shortcuts import render, get_object_or_404
from .models import *
from .forms import *
from django.contrib.auth.decorators import login_required
from django.shortcuts import redirect
from django.contrib import messages

def principal_list(request):
    return render(request, 'entrega/principal_list.html', {})

@login_required
def camion_list(request):
    camiones = Camion.objects.all()
    return render(request, 'entrega/camion_list.html', {'camiones': camiones})
@login_required
def piloto_list(request):
    pilotos = Piloto.objects.all()
    return render(request, 'entrega/piloto_list.html', {'pilotos': pilotos})
@login_required
def paquete_list(request):
    paquetes = Paquete.objects.all()
    return render(request, 'entrega/paquete_list.html', {'paquetes': paquetes})

def camion_detail(request, pk):
    camion = get_object_or_404(Camion, pk=pk)
    return render(request, 'entrega/camion_detail.html', {'camion': camion})

def piloto_detail(request, pk):
    piloto = get_object_or_404(Piloto, pk=pk)
    return render(request, 'entrega/piloto_detail.html', {'piloto': piloto})

def paquete_detail(request, pk):
    paquete = get_object_or_404(Paquete, pk=pk)
    return render(request, 'entrega/paquete_detail.html', {'paquete': paquete})

@login_required
def paquete_remove(request, pk):
    paquete = get_object_or_404(Paquete, pk=pk)
    paquete.delete()
    return redirect('paquete_list')

@login_required
def piloto_remove(request, pk):
    piloto = get_object_or_404(Piloto, pk=pk)
    piloto.delete()
    return redirect('piloto_list')

@login_required
def camion_remove(request, pk):
    camion = get_object_or_404(Camion, pk=pk)
    camion.delete()
    return redirect('camion_list')

@login_required
def ciudad_remove(request, pk):
    ciudad = get_object_or_404(Ciudad, pk=pk)
    ciudad.delete()
    return redirect('ciudad_list')

@login_required
def camion_new(request):
    if request.method == "POST":
        camionform = CamionForm(request.POST)
        if camionform.is_valid():
            camion = camionform.save(commit=False)
            camion.save()
            return redirect('camion_detail', pk=camion.pk)
    else:
        camionform = CamionForm()
    return render(request, 'entrega/camion_edit.html', {'camionform': camionform})
@login_required
def piloto_new(request):
    if request.method == "POST":
        pilotoform = PilotoForm(request.POST)
        if pilotoform.is_valid():
            piloto = pilotoform.save(commit=False)
            piloto.save()
            return redirect('piloto_detail', pk=piloto.pk)
    else:
        pilotoform = PilotoForm()
    return render(request, 'entrega/piloto_edit.html', {'pilotoform': pilotoform})

@login_required
def paquete_new(request):
    if request.method == "POST":
        paqueteform = PaqueteForm(request.POST)
        if paqueteform.is_valid():
            paquete = paqueteform.save(commit=False)
            paquete.save()
            return redirect('paquete_detail', pk=paquete.pk)
    else:
        paqueteform = PaqueteForm()
    return render(request, 'entrega/paquete_edit.html', {'paqueteform': paqueteform})

@login_required
def camion_edit(request, pk):
    camion = get_object_or_404(Camion, pk=pk)
    if request.method == "POST":
        camionform = CamionForm(request.POST, instance=camion)
        if camionform.is_valid():
            camion = camionform.save(commit=False)
            camion.save()
            return redirect('camion_detail', pk=camion.pk)
    else:
        camionform = CamionForm(instance=camion)
    return render(request, 'entrega/camion_edit.html', {'camionform': camionform})

@login_required
def piloto_edit(request, pk):
    piloto = get_object_or_404(Piloto, pk=pk)
    if request.method == "POST":
        pilotoform = PilotoForm(request.POST, instance=piloto)
        if pilotoform.is_valid():
            piloto = pilotoform.save(commit=False)
            piloto.save()
            return redirect('piloto_detail', pk=piloto.pk)
    else:
        pilotoform = PilotoForm(instance=piloto)
    return render(request, 'entrega/piloto_edit.html', {'pilotoform': pilotoform})

@login_required
def paquete_edit(request, pk):
    paquete = get_object_or_404(Paquete, pk=pk)
    if request.method == "POST":
        paqueteform = PaqueteForm(request.POST, instance=paquete)
        if paqueteform.is_valid():
            paquete = paqueteform.save(commit=False)
            paquete.save()
            return redirect('paquete_detail', pk=paquete.pk)
    else:
        paqueteform = PaqueteForm(instance=paquete)
    return render(request, 'entrega/paquete_edit.html', {'paqueteform': paqueteform})

@login_required
def ciudad_list(request):
    ciudades = Ciudad.objects.all()
    return render(request, 'entrega/ciudad_list.html', {'ciudades': ciudades})

@login_required
def ciudad_nueva(request):
    if request.method == "POST":
        formulario = CiudadForm(request.POST)
        if formulario.is_valid():
            ciudad = Ciudad.objects.create(nombre=formulario.cleaned_data['nombre'])
            for paquete_id in request.POST.getlist('paquete'):
                asignacion = Asignacion(paquete_id=paquete_id, ciudad_id = ciudad.id)
                asignacion.save()

            messages.add_message(request, messages.SUCCESS, 'Asignacion Guardada Exitosamente')
            return redirect('ciudad_list')

    else:
        formulario = CiudadForm()
    return render(request, 'entrega/ciudad_editar.html', {'formulario': formulario})

def ciudad_edit(request, pk):
    ciudad = get_object_or_404(Ciudad, pk=pk)
    if request.method == "POST":
        formulario = CiudadForm(request.POST, request.FILES, instance=ciudad)
        if formulario.is_valid():
            ciudad = formulario.save(commit=False)
            ciudad.save()
            return redirect('ciudad_list')

    else:
        formulario = CiudadForm(instance=ciudad)
    return render(request, 'entrega/ciudad_editar.html', {'formulario': formulario})
