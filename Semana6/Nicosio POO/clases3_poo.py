class Producto2:
    def __init__(self):
        self.cantidad=10
        self._costo=5           # Es simbolico.Etica programador
        self.__impuesto=0.16    #Se crea el "name mangling"
        
pera=Producto2()
# print(pera.cantidad, pera._costo)    # Imprime sin inconveniente       
# print(pera.__impuesto)       # Indica que ese atributo no lo posee la instancia. Da la sensacion de "privado", pero realmente se aplica el "name mangling" por los 2 guines bajos en el atributo impuesto.

# print(dir(pera))     # Podemos apreciar que al atributo __impuesto se le antepone el nombre "_Producto2"  
print(pera._Producto2__impuesto)       # Se le invoca con el nombre correcto.
        