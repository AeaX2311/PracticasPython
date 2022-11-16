from django.forms import ModelForm, EmailInput
from Personas.models import Persona

class PersonaForm(ModelForm):
    class Meta:
        model = Persona;
        fields = '__all__';
        widgets = {
            'correoElectronico': EmailInput(attrs={'type':'email'})
        };