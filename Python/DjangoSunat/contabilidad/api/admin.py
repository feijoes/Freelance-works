from django.contrib import admin
from .models import VerificarRuc, RucVerificado

# Register your models here.
admin.site.register(RucVerificado)
admin.site.register(VerificarRuc)