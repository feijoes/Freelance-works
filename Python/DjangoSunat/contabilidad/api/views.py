
from django.shortcuts import render
from .libs import validar_ruc, validar_numero_ruc
from django.core.handlers.wsgi import WSGIRequest

from .forms import VericarRucForm, RucNForm
from .models import NRuc_info, RucVerificado

def index(request: WSGIRequest):

    
    if request.method == "POST":
        new_Verificar = VericarRucForm(request.POST)
        
        if new_Verificar:	

            response = validar_ruc(request.POST)

            if response["success"]:
                a = validar_numero_ruc(request.POST["numRuc"])[1]
                exits =  NRuc_info.objects.filter(ruc=request.POST["numRuc"])
                if not exits.exists():
                    a["ruc"] = request.POST["numRuc"]
                    b = NRuc_info.objects.create(**a)
                else:
                    b = exits.first()
                    
                print(response["data"])
                RucVerificado.objects.create(razonSocial=b.nombre ,
                                             estadoCp=response["data"].get("estadoCp","NO EXISTE") ,
                                             estadoRuc=response["data"].get("estadoRuc","ACTIVO") ,
                                             condDomiRuc=response["data"].get("condDomiRuc","HABIDO"),
                                             ruc_info=b)
                print(b.nombre)
                return render(request, "validarRuc.html",{'form':VericarRucForm(initial=request.POST.items()),"messageValido" : "Es valido", "razon": b.nombre})
        return render(request, "validarRuc.html",{'form':VericarRucForm(initial=request.POST.items()), "messageNoValido": "NO es valido"})



    form = VericarRucForm() 
    return render(request, "validarRuc.html",{'form':form})

def Ruc(request: WSGIRequest):
    
    if request.method == "POST":
        
        
        response = validar_numero_ruc(request.POST["ruc"])
    
        if response[0]:
            info: dict[str,any] = response[1]
            info["ruc"] = request.POST["ruc"]
            NRuc_info.objects.create(**info)
            return render(request,"n_ruc.html",{"form": RucNForm(initial=request.POST),"messageValido": "Ruc valido","info":response[1]})
        
        return render(request,"n_ruc.html",{"form": RucNForm(initial=request.POST),"messageNoValido": response[1]["error"]})
        

    return render(request, "n_ruc.html",{"form":RucNForm()})

        