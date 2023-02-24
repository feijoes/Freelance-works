from django import forms
from .models import VerificarRuc

class VericarRucForm(forms.ModelForm):
   class Meta:  
        model = VerificarRuc  
        fields = "__all__"  