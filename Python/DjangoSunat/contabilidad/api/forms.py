from django import forms
from .models import VerificarRuc

class VericarRucForm(forms.ModelForm):
   class Meta:  
      model = VerificarRuc  
      fields = "__all__"  
      

   

class RucNForm(forms.Form):
   ruc = forms.CharField(label='Numero de Ruc', max_length=11)