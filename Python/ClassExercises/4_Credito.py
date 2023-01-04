class Credito():
    def __init__(self,titular,nCuotas,total,saldo):
        self.titular = titular
        self.nCuotas = nCuotas
        self.total = total
        self.saldo = saldo
        self.estado = "vigente"
    
    def actualizarEstado(self):
        listaParaPagar = []
        for i in self.nCuotas():
            if i.estado == "pendiente":
                listaParaPagar.append(i)
        if listaParaPagar:
            self.estado = "cancelado"
        else:
            self.estado = "vigente"
        
        
    def pagar(self):
        for i in self.nCuotas:
            self.total -= i.total_a_pagar
            i.actualizarEstado()
        self.actualizarEstado
    
class Cuota():
    def __init__(self,nCuota,monto_a_pagar):
        self.nCuota = nCuota
        self.monto_a_pagar = monto_a_pagar
        self.estado = "pendiente"
  
        
    def actualizarEstado(self):
        
        if self.estado == "pagado":
            self.estado = "pendiente"
        else: 
            self.estado = "pagado"