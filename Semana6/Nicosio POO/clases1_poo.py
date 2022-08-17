import math

class Vector:
    #creamos un metodo que recibe parametros
    def inicializa(self, x, y):
        self.x=x
        self.y=y
    
    #creamos otro metodo
    def muestra(self):
        print("Muestra valores x,y: ", self.x, self.y)
        
    #creamos un metodo que nos regresa un valor
    def magnitud(self):
        return math.sqrt(self.x**2+self.y**2)        
    
#creamos una instancia
v1=Vector()

#Invocamos los metodos
v1.inicializa(4, 5)   #invocamos este metodo para pasar los valores de los parametros 
v1.muestra()
print(v1.magnitud().__round__(3))   # podemos imprimir directamente o el resultado asignarlo a una variable que decidamos
