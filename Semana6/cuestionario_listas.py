""" lista_compras = ["pan", "huevo", "queso", "arroz", "jamon"]
print(lista_compras)
lista_compras.append("maní")    # Adiciona 'mani' al final de la lista
print(lista_compras)
lista_compras.remove("arroz")# Elimina 'arroz' y los demas elementos se mueven a la izquierda
print(lista_compras)
lista_compras.insert(2,"leche")# Inserta 'leche' en posicion 2 y los demas se mueven a derecha
print(lista_compras) """


""" datos = ["semillas", 500, "cerveza", 2, "despacho", 4100, "pago", "bitcoin", "confianza", 95.4]
trozo = datos[1:9:2]
print(trozo) """


# Cual funcion devuelve el nombre del valor mas grande.
""" def ganador(votos):              # Primer caso. Imprime nombre del mayor (Marcela)
    mayor = votos[0]
    for cand in votos:
        if cand[1] > mayor[1]:
            mayor = cand
    return mayor[0] """


""" def ganador(votos):               # Segundo caso. Imprime nombre del menor (Loreto)
  mayor = votos[0]
  for cand in votos:
    if cand[1] < mayor[1]:
      mayor = cand
  return mayor[0] """


""" def ganador(votos):                 # Tercer caso. Imprime numero mayor (40)
  mayor = votos[0]
  for cand in votos:
    if cand[1] > mayor[1]:
      mayor = cand
  return mayor[1] """


""" def ganador(votos):                 # Cuarto caso. Imprime nombre y valor mas grande
  mayor = votos[len(votos)-1]           # [Marcela, 40]
  for cand in votos:
    if cand[1] >= mayor[1]:
      mayor = cand
  return mayor """


""" def ganador(votos):                     # Quinto caso. Imprime nombre y valor mas grande
  mayor = votos[0]                      # [Marcela, 40]
  for cand in votos:
    if cand[1] > mayor[1]:
      mayor = cand
  return mayor

resultados = [ ["Alfredo",20], ["Marcela",40], ["Ignacio",30], ["Loreto",10] ]
mayoria = ganador(resultados) """


#Tablero de 3 x 3 posiciones y numerado del 1 al 9. Cual codigo me permite recorrer el tablero por orden de columnas. La salida debe escribir...1 4 7 2 5 8 3 6 9 
""" print()
tablero = [ [1,2,3], [4,5,6], [7,8,9] ]
print(tablero)
print() """

""" for j in range(3):           #Imprime los elementos en el mismo orden. 1 2 3 4 5 6 7 8 9
  for i in range(3):
    print(tablero[j][i],end=" ") """
    
    
""" for j in range(3):               #Imprime los elementos en este orden. 1 4 7 2 5 8 3 6 9 
  for i in range(3):
    print(tablero[i][j],end=" ") """


""" for i in range(3):               #Imprime los elementos en el mismo orden. 1 2 3 4 5 6 7 8 9
  for j in range(3):
    print(tablero[i][j],end=" ") """


""" for i in range(9):                 #Imprime los elementos en este orden. 1 4 7 2 5 8 3 6 9
  print(tablero[i%3][i//3],end=" ") """

""" for i in range(3):                 #Imprime los elementos en este orden. 1 4 7 2 5 8 3 6 9
  for j in range(3):
    print(tablero[j][i],end=" ") """
    

#Obtener la cantidad de veces que un elemento 'elem' se encuentra dentro de la lista conjunto.

""" def cuantas(elem, conjunto):                  # Funciona
  contador = 0
  for e in conjunto:
    if e == elem:
      contador += 1
  return contador """
  

""" def cuantas(elem, conjunto):        # Cuenta el numero total de elementos en el conjunto
  contador = 0
  for k in range(len(conjunto)):
    contador += 1
  return contador """
  

""" def cuantas(elem, conjunto):           # Cuenta el tamaño del conjunto
  return len(conjunto) """


""" def cuantas(elem, conjunto):            # Funciona
  contador = 0
  for k in range(len(conjunto)):
    if conjunto[k] == elem:
      contador += 1
  return contador """

""" def cuantas(elem, conjunto):               # Devuelve el numero que se esta buscando como repetido
  for e in conjunto:
    if e == elem:
      return e

numeros = [1, 8, 7, 9, 1, 5, 4, 1, 9, 9, 1, 7, 1]
print(numeros)
print()
print(cuantas(1,numeros))   """   

#valor de la variable splitted luego de ejecutar el siguiente código.
# ['Marcelo, Alvaro', ' Elena, Karen', ' Jaime', ' Carmen']

""" contactos = "Marcelo, Alvaro; Elena, Karen; Jaime; Carmen"
splitted = contactos.split(";")
print()
print(splitted)
print() """


""" 
datos = [2, "Julio", 2017, "Final", 14.5, "Chile", 0, "Alemania", 1]
trozo = datos[2:6]
print(trozo) """

# Debe arrojar [49, 2, 55, 300]
# unidades = [40, 32, 49, 2, 20, 8, 55, 300, 10]
# muestra = unidades[2:8:2]                                                 # Imprime  [49, 20, 55]
# muestra = unidades[2:4] + unidades[6:8]                                     # Imprime  [49, 2, 55, 300]
# muestra = unidades[2:3] + unidades[3:7:3] + unidades[7:8]                   # Imprime  [49, 2, 55, 300]
# print(muestra)



#Escriba una función de nombre promedio_std(). La función debe recibir una lista de números llamada lista, y debe retornar retornar el promedio de ellos, junto con su desviación estándar.
#La desviación estándar corresponde a la raíz de la suma de los cuadrados de las diferencias de cada elemento respecto al promedio, divididos por la cantidad de elementos.

# def promedio_std(lista):
#   cant = len(lista)
#   acum = 0
#   for n in lista:
#     acum += n
#   x = acum/cant
  
#   acumul = 0
#   for n in lista:
#     cuadrados = (n-x)**2
#     acumul += cuadrados
#     previoRaiz = acumul/cant
#     y = previoRaiz**(1/2)
#   return (x,y)

  
# lista = [12, 25, 38, 49, 57, 64, 73]
# print(promedio_std(lista))

#Escriba una función color_frecuente que reciba como argumento a una lista de strings llamada lista y retorne el string más repetido y el número de ocurrencias del mismo.
#Por ejemplo para la lista ['azul', 'rojo', 'verde', 'verde', 'verde', 'rojo', 'verde', 'verde', 'azul', 'amarillo', 'azul', 'azul', 'verde', 'verde', 'verde', 'amarillo', 'amarillo']
#Debe retornar: "verde", 8
# prioridad: azul, rojo, verde, amarillo


def color_frecuente(lista):
#determino un diccionario con sus colores y numero de veces cada uno
  frecuencia = {}
  for c in lista:
    if c in frecuencia:
      frecuencia[c] += 1
    else:
      frecuencia[c] = 1
      
  #determino cual es el numero mas alto dentro de los valores del diccionario
  max = 0
  for clave, valor in frecuencia.items():
    if valor > max:
      max = valor
  # print("Valor mayor", max)    

  #luego con ese valor maximo que encontre determino que pareja tiene ese valor. En caso de empate entre varios colores como valor mas alto pongo a recorrer cada llave (es decir cada color) dentro mi lista de prioridades para con ello conseguir solo imprimir una pareja.
  if max in frecuencia.values():
    for clave in frecuencia:
      prio_list = ['azul', 'rojo', 'verde', 'amarillo']
      for clave in prio_list :
        if frecuencia[clave] == max:
          return clave,max


lista = ['azul', 'azul', 'azul', 'verde', 'rojo', 'verde', 'verde', 'azul', 'amarillo', 'azul', 'verde', 'verde', 'verde', 'amarillo', 'amarillo']

print(color_frecuente(lista))







  
  
  
  
  

#Crear una función buscaminas que reciba como argumento a una tablero tablero y dos coordenadas i, j, y que entregue la cantidad de bombas que rodean a esa posición. 
#tablero = [[' ', 'X', ' ', 'X'],['X', ' ', ' ', ' '],[' ', 'X', 'X', ' '],['X', ' ', ' ', 'X']]
#Por ejemplo, si la el tablero dado es el representado en la tabla, y la posición viene dada por i=0 y j=0, tu función debe retornar el valor 2, ya que hay dos bombas rodeándola, en (0,1) y (1,0). 
#Por otro lado, si el tablero es el mismo, y las coordenadas son i=1, j=1, tu función debe retornar 4, pues hay bombas rodeando la posición en (1,0), en (0,1), en (2,1) y en (2,2).
""" row = len(tablero)         # Corresponde a la fila
col = len(tablero[0])      # Corresponde a la columna
 """

 
# def buscaminas(tablero,i,j):
#   bombas = []
#   actual = tablero[i][j]
#   # print(f"Bombas encontradas alrededor de la posicion[{i}][{j}] = ", end="")
  
#   fila = i
#   columna = j+1
#   if columna==4:
#     derecha = " "
#     bombas.append(derecha)
#   else:
#     derecha = tablero[fila][columna]
#     bombas.append(derecha)

#   fila = i
#   columna = j-1
#   if columna==-1:
#     izquierda = " "
#     bombas.append(izquierda)
#   else:
#     izquierda = tablero[fila][columna]
#     bombas.append(izquierda)

#   fila = i+1
#   columna = j
#   if fila==4:
#     abajo = " "
#     bombas.append(abajo)
#   else:
#     abajo = tablero[fila][columna]
#     bombas.append(abajo)

#   fila = i+1
#   columna = j+1
#   if fila==4 or columna==4:
#     abajo_derecha = " "
#     bombas.append(abajo_derecha)
#   else:
#     abajo_derecha = tablero[fila][columna]
#     bombas.append(abajo_derecha)

#   fila = i+1
#   columna = j-1
#   if fila==4 or columna==-1:
#     abajo_izquierda = " "
#     bombas.append(abajo_izquierda)
#   else:
#     abajo_izquierda = tablero[fila][columna]
#     bombas.append(abajo_izquierda)

#   fila = i-1
#   columna = j
#   if fila==-1:
#     arriba = " "
#     bombas.append(arriba)
#   else:
#     arriba = tablero[fila][columna]
#     bombas.append(arriba)

#   fila = i-1
#   columna = j+1
#   if fila==-1 or columna==4:
#     arriba_derecha = " "
#     bombas.append(arriba_derecha)
#   else:
#     arriba_derecha = tablero[fila][columna]
#     bombas.append(arriba_derecha)

#   fila = i-1
#   columna = j-1
#   if fila==-1 or columna==-1:
#     arriba_izquierda = " "
#     bombas.append(arriba_izquierda)
#   else:
#     arriba_izquierda = tablero[fila][columna]
#     bombas.append(arriba_izquierda)

  
#   return bombas.count("X")
 

# tablero = [[' ', 'X', ' ', 'X'],['X', ' ', ' ', ' '],[' ', 'X', 'X', ' '],['X', ' ', ' ', 'X']]

# print(buscaminas(tablero,3,2))



