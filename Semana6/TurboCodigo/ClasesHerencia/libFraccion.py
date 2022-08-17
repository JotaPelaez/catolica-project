class Fraccion: 
  
  def __init__(self, num=0, den=1):
    if isinstance(num,int):
      self.num = num            
    else: 
      self.num=0
    if isinstance(den,int) and den!=0:
      self.den = den            
    else: 
      self.den=1    
    self.simplifica()
          
  def __str__(self):
    return "(" + str(self.num) + "/" + str(self.den) + ")"
    
  def __mul__(self, obj):
    n = self.num * obj.num
    d = self.den * obj.den
    x = Fraccion(n,d)
    x.simplifica()
    return x
  
  def __div__(self, obj):
    n = self.num * obj.den
    d = self.den * obj.num
    x = Fraccion(n,d)
    x.simplifica()
    return x

  def __add__(self, obj):
    n = self.num * obj.den + self.den * obj.num 
    d = self.den * obj.den
    x = Fraccion(n,d)
    x.simplifica()
    return x
  
  def __sub__(self, obj):
    n = self.num * obj.den + self.den * obj.num 
    d = self.den * obj.den
    x = Fraccion(n,d)
    x.simplifica()
    return x
  
  def __eq__(self, b):
    if self.num/self.den == b.num/b.den:
      return True
    else:
      return False

  def simplifica(self):
    d=self.mcd(self.num,self.den)
    self.num=int(self.num/d)
    self.den=int(self.den/d)

  def mcd(self,a,b):
    if b==0:
      return a
    else:
      return self.mcd(b,a%b)


#XXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXX 
""" print() 
#De dos numeros es el entero maximo que puede dividir a dos numeros sin dejar residuo.
#Usando el ciclo while
def maximo_comun_divisor(a, b):
    temporal = 0
    while b != 0:
        temporal = b
        b = a % b
        a = temporal
    return a

print("MCD usando ciclo while:", maximo_comun_divisor(20, 6))
print()
#Usando recursion
def maximo_comun_divisor_recursivo(a, b):
    if b == 0:
        return a
    return maximo_comun_divisor_recursivo(b, a % b)
print(f"MCD usando recursion: {maximo_comun_divisor(20, 6)}")
print() """
