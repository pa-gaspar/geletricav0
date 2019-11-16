from django import forms
from .models import carga, cargaTipo, local, area
'''
class cargaForm(forms.ModelForm):

    tipoDaCarga = forms.ChoiceField( choices = cargaTipo.objects.all().values_list('nome','nome'), required=True)    
    descricao = forms.CharField(max_length=300)
    potencia = forms.IntegerField()
    cargaChave = forms.ModelChoiceField(local.objects.all(),required=True)
    class Meta:
        model = carga
        fields = [
            'tipoDaCarga',
            'descricao',
            'potencia',
            'cargaChave'
        ]

    def erro_potencia(self,*args,**kwargs):
        pot = self.cleaned_data.get('potencia')
        if pot < 0 :
            raise forms.ValidationError("Não é'permitido potência negativa")
        return pot
'''        
    
class cargaForm(forms.ModelForm):
    class Meta:
        model = carga
        fields = ["tipoDaCarga", "descricao", "potencia","chaveCarga"]
        #fields = [ "descricao", "potencia","chaveCarga"]