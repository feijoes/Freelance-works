class Producto():
    
    def __init__(self,nombre,cantidad,precio):
        self.nombre = nombre
        self.cantidad = cantidad
        self.precio = precio

    def getNombre(self):
        return self.nombre
    
    def setNombre(self,nombre):
        self.nombre = nombre
    
    def getCantidad(self):
        return self.cantidad

    def setCantidad(self,cantidad):
        self.cantidad = cantidad
    
    def getPrecio(self):
        return self.precio
    
    def setPrecio(self,precio):
        self.precio = precio
        
    def valor(self):
        return self.getCantidad() * self.getPrecio()
    
Coca =  Producto("Coca cola",5,2)
Galleta = Producto("Galleta Soda",10,0.5)
Leche = Producto("Leche Gloria",2,3.5)
listaProductos = [Coca,Galleta,Leche]

MayorValor = listaProductos[0]
for i in listaProductos:

    if i.valor() > MayorValor.valor():
        MayorValor = i

print(f"{MayorValor.getNombre()} tiene el mayor valor, de {MayorValor.valor()}")