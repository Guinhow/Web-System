from django import forms
from .models import DadosFormulario

class FormularioDados(forms.ModelForm):
    class Meta:
        model = DadosFormulario
        fields = '__all__'

class ConsultaForm(forms.Form):
    id = forms.IntegerField(required=False)
    codigo_bq = forms.IntegerField(required=False)
    data_coleta = forms.DateField(required=False)
    data_entrada = forms.DateField(required=False)
    cliente = forms.CharField(max_length=45, required=False)
    codigo_amostra = forms.IntegerField(required=False)
    amostra = forms.CharField(max_length=45, required=False)
    data_entrada = forms.DateField(required=False)
    peso = forms.IntegerField(required=False)
    temperatura = forms.IntegerField(required=False)
    classificacao = forms.CharField(max_length=10, required=False)
    obs = forms.CharField(required=False)