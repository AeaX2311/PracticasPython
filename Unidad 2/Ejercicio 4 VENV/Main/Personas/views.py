from django.shortcuts import get_object_or_404, redirect, render
from django.shortcuts import render, get_object_or_404
from Personas.forms import PersonaForm
from Personas.models import Persona

# Create your views here.
def detallePeronsa(req, id) :
    persona = get_object_or_404(Persona, pk = id);
    return render(req, 'Detalle.html', {'persona': persona});

def nuevaPersona(req) :
    if req.method == "POST":
        formaPersona = PersonaForm(req.POST);

        if formaPersona.is_valid():
            formaPersona.save();
            return redirect('index');
    else:
        formaPersona = PersonaForm();
        return render(req, 'Agregar.html', {'formaPersona': formaPersona})

def editarPersona(req, id):
    persona = get_object_or_404(Persona, pk = id);
    if req.method == "POST":
        formaPersona = PersonaForm(req.POST, instance = persona);

        if formaPersona.is_valid():
            formaPersona.save();
            return redirect('index');
    else:
        formaPersona = PersonaForm(instance = persona);
        return render(req, 'Editar.html', {'formaPersona': formaPersona})

def eliminarPersona(req, id):
    persona = get_object_or_404(Persona, pk = id);
    if persona:
        persona.delete();
        return redirect('index');