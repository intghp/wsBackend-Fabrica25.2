from django import forms
from .models import Cidade, ConsultaTempo

class CidadeForm(forms.ModelForm):
    class Meta:
        model = Cidade
        fields = ['nome', 'pais']
        
class ConsultaTempoForm(forms.ModelForm):
    class Meta:
        model = ConsultaTempo
        fields = ['cidade']