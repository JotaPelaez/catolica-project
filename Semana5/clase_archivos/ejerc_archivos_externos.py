#Queremos comparar el tiempo que tarda en sumar todos los elementos de una lista, un bucle for y un bucle while.
#Para ello, debemos calcular el tiempo empleado en cada bucle varias veces y luego promediarlo. Debemos cronometrar lo que tarda cada bucle 100 veces y guardar cada resultado en un archivo.

import time, random
# Creamos una lista de 50.000 datos, cuyos numeros los tomo aleatoriamente dentro de un rango de cero a 150.000
lista = []               
for x in range(50000):
    lista.append(random.randint(0, 150000))
# Abrimos archivo en modo escritura
fichero = open("./Semana5/clase_archivos/times.txt", "wt", encoding="utf-8") 
# Recorremos 100 numeros de la lista y medimos el tiempo para cada numero desde que inicia 'startTime' hasta que termina 'elapsedTime'. Primero para el bucle FOR
for x in range(100):              
    accFor = 0
    startTime = time.time()
    for num in lista:
        accFor = accFor + num
    elapsedTimeFor = time.time() - startTime
# Recorremos 100 numeros de la lista y medimos el tiempo para cada numero desde que inicia 'startTime' hasta que termina 'elapsedTime'. Segundo para el bucle WHILE
    pos = 0
    accWhile = 0
    starTime = time.time()
    
    while pos < len(lista):
        accWhile = accWhile + lista[pos]
        pos = pos + 1
    elapsedTimeWhile = time.time() - starTime
# Finalmente escribimos el tiempo del FOR y el WHILE cada vez y por 100 veces en el archivo 'times.txt'. Al final de cada linea adicionamos un salto de linea '\n'
    fichero.write(f"{elapsedTimeFor};{elapsedTimeWhile}\n")
#Cerramos nuestro archivo de trabajo
fichero.close()
#Abrimos en modo lectura el archivo que recien creamos 'times.txt'
fichero = open("./Semana5/clase_archivos/times.txt", encoding="utf-8")
#A continuacion vamos a calcular un promedio. Sumamos los tiempos y lo dividimos entre el numero de lineas leidas ( o el numero de veces en otras palabras).
#Para ello incializamos en cero las variables de promedio del for y while, asi como la variable correspondiente al numero de veces por el que se dividirá. 
meanFor = 0
meanWhile = 0
samples = 0
#Utilizamos un ciclo for para ir leyendo cada una de las lineas en el archivo, le retiramos el string salto de linea '\n' que le agregamos cuando escribimos nuestro archivo anteriormente y por ultimo por cada linea leida hacemos una division de cada dato y lo asignamos a variables diferentes ( una para el tiempo for y otra para el tiempo while).  
for line in fichero.readlines():
    line.replace("\n", "")
    timeFor, timeWhile = line.split(";")
    meanFor += float(timeFor)                # Emezamos a sumar los tiempos FOR
    meanWhile += float(timeWhile)            # Empezamos a sumar los tiempos WHILE
    samples += 1                             # Vamos sumando las veces x la que dividiremos
# Al final calculamos el promedio del FOR y WHILE. Multiplicamos por 10³ para ver la respuesta en milisegundos (ms)
print(f"Tiempo for: {(meanFor/samples)*(10**3)}ms. Tiempo while: {(meanWhile/samples)*(10**3)}ms.")
fichero.close()

    
    
    
