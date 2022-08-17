class Vector:
    
    def inicializa(self):
        self.x=1
        self.y=5
    
    
v1=Vector()
v1.inicializa()
print()
print("Valores iniciales (x,y): ", v1.x, v1.y)
v1.x=52
print("Valor de X cambiado (x,y): ", v1.x, v1.y)

print()
v2=Vector()
v2.inicializa()
print("Valores iniciales (x,y): ", v2.x, v2.y)
v2.x=3
v2.y=7
print("Valores cambiados (x,y): ", v2.x, v2.y)
print()

#Puedo crear un atributo adicional sobre el objeto, NO sobre la clase.
v1.z=15
print("Valor de Z adicionado (x,y,z): ", v1.x, v1.y, v1.z)
