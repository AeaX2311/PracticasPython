from django.shortcuts import render

from Personas.models import Persona

# Create your views here.
def personaView(req):
    personas = Persona.objects.order_by('id');
    return render(req, 'Personas.html', {'personas':personas});