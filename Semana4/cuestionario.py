# print()
# def mcd(n1,n2):
#     ver = False
#     if (n2 < n1):                   
#         aux = n1
#         n1 = n2
#         n2 = aux     
#     i = n1         
#     while not ver and i >= 1 :
#         if n1 % i == 0 and n2 % i == 0:
#             ver = True
#         else:
#             i -= 1

#     return i

# print(mcd(10,15))
# print()

# ----XXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXX

# def max_potencia(n):
# print()
# max=2
# for i in range(1,15):
#   potencia=2**i
#   if potencia>=max:
#     max=potencia
#     if potencia>1020:
#       print(i-1)
#       break
  
# print()

# max_potencia(65)

# ----XXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXX

# print()
# def exponente(n):
#   i=0
#   while i<=n:
#     max=2
#     potencia=2**i
#     # print(i,"-",potencia)
#     if potencia>=max:
#       max=potencia
#       if max>n:
#         resultado=i-1
#         print(resultado)
#         break
#     i+=1

# exponente(1697)
# print()

# ----XXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXX
# def panprimo(n):
#   n=str(n)
#   num_cero=n.count("0")
#   num_uno=n.count("1")
#   num_dos=n.count("2")
#   num_tres=n.count("3")
#   num_cuatro=n.count("4")
#   num_cinco=n.count("5")
#   num_seis=n.count("6")
#   num_siete=n.count("7")
#   num_ocho=n.count("8")
#   num_nueve=n.count("9")
#   if num_cero>=1 and num_uno>=1 and num_dos>=1 and num_tres>=1 and num_cuatro>=1 and num_cinco>=1 and num_seis>=1 and num_siete>=1 and num_ocho>=1 and num_nueve>=1:
#     num_pri=int(n)%1000
#     if num_pri==1:
#       return False
#     elif num_pri==2:
#       return True
#     else:
#       for i in range(2, num_pri):
#         if num_pri%i==0:
#           return False
#       return True 
#   else:
#     return False

# print()
# print(panprimo(2424643))
# print()
# print(panprimo(1234567890))
# print()
# print(panprimo(10123485769))
# print()


# Saber si un numero es primo
print()
n=int(input("Ingrese un numero: "))
x=1
c=0
while x<=n:
  if n%x==0:
    c+=1
  x+=1

if c==2:
  print(f"El numero {n} es primo")
else:
  print(f"El numero {n} NO es primo")

print()