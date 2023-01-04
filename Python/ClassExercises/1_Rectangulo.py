
class Rectangulo():
    
    def __init__(self,base,altura):
        self.base = base
        self.altura = altura
    
    def area(self):
        return self.base * self.altura
    
    def perimetro(self):
        return self.base * 2 + self.altura * 2
    
    def mostrarDatos(self):
        print(f"Rectangulo con base {self.base} y altura: {self.altura} tiene area de {self.area()} y {self.perimetro()} de perimetro")
        
rec1 = Rectangulo(3.8,2.9)
rec2 = Rectangulo(1,2)

rec1.mostrarDatos()
rec2.mostrarDatos()