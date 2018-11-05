from django import forms
from .models import *

class CamionForm(forms.ModelForm):
    class Meta:
        model = Camion
        fields = ('marca','modelo' ,'matricula', 'tipo')

class PilotoForm(forms.ModelForm):
    class Meta:
        model = Piloto
        fields = ('camion','nombre','direccion','telefono','salario')

class PaqueteForm(forms.ModelForm):
    class Meta:
        model = Paquete
        fields = ('piloto','destinatario','direccion','descripcion')

class CiudadForm(forms.ModelForm):

    class Meta:
        model = Ciudad
        fields = ('nombre','paquete')

        def __init__ (self, *args, **kwargs):
            super(CiudadForm, self).__init__(*args, **kwargs)
            self.fields["paquete"].widget = forms.widgets.CheckboxSelectMultiple()
            self.fields["paquete"].help_text = "Ingrese los paquetes"
            self.fields["paquete"].queryset = Paquete.objects.all()
