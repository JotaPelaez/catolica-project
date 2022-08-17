import math

class Vector:
    #creamos el metodo __init__ (llamado constructor). Para inicializar atributos
    def __init__(self, x, y):    # puedo pasar valores default (self, x=5, y=5)
        self.x=x
        self.y=y
    
    #creamos otro metodo
    def muestra(self):
        print("Muestra valores x,y: ", self.x, self.y)
        
    #creamos un metodo que nos regresa un valor
    def magnitud(self):
        return math.sqrt(self.x**2+self.y**2)        
    
#cuando instanciamos, podemos pasar los parametros del metodo __init__
v1=Vector(4, 5)

v1.muestra()
h=v1.magnitud()
print(h.__round__(4))
