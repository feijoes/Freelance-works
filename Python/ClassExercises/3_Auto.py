class Auto():
    
    def __init__(self,nMantenimientos,kilometraje):
        self.nMantenimientos = nMantenimientos
        self.kilometraje = kilometraje
    
    def getNroMantenimientos(self):
        return self.nMantenimientos
    
    def setNroMantenimientos(self,nMantenimientos):
        self.nMantenimientos = nMantenimientos
        
    def getKilometraje(self):
        return self.kilometraje

    def setKilometraje(self,kilometraje):
        self.kilometraje = kilometraje
    
    def viaje(self,kilometros):
        self.kilometraje += kilometros
        
    def mantenimiento(self):
        self.nMantenimientos +=1
        
    def necesita_Mantenimiento(self):
        
        return (self.kilometraje / 5000) >= self.nMantenimientos +1
    def evaluarAuto(self):
        if self.necesita_Mantenimiento():
            print("Auto necesita de un mantenimiento")
        else:
            print("Auto no necesita de un mantenimiento")
    
auto1 = Auto(0,0)
auto1.evaluarAuto()
auto1.viaje(2500)
auto1.evaluarAuto()
auto1.viaje(2500)
auto1.evaluarAuto()
auto1.mantenimiento()
auto1.evaluarAuto()