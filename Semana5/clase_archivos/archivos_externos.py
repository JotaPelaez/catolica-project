#ABRIR Y LEER DOCUMENTO EXISTENTE.
# El archivo 'demo.txt' originalmente tiene las siguientes 3 lineas:
#Esta es una acción de trabajo con archivos externos.
#También sirve como referencia de estudio.
#Y por último voy verificando cada paso en linea. 

# MODO LECTURA UNICAMENTE
# 1. Abro el archivo 'demo.txt' y lo asigno a una variable para poder invocar metodos.
fichero = open("./Semana5/clase_archivos/demo.txt", "r", encoding="utf-8")

# 2. Procedo a leer el archivo.
# Para leer LINEA a LINEA podemos usar el metodo READLINE. Cada llamada nos devolvera una nueva linea hasta llegar al final del archivo 'demo.txt'.
primerLinea = fichero.readline()
# # Puedo asignar esta lectura a una variable, para despues trabajar con ella si lo necesito.
print(primerLinea)
# # A continuacion podemos seguir invocando el metodo readline y nos leera la siguiente linea y asi sucesivamente hasta terminar de leer por completo todo el archivo 'demo.txt'
print(fichero.readline())    # imprime segunda linea. Tiene salto de linea. OJO
print(fichero.readline())    # imprime tercera linea. No muestra salto de linea. OJO

# Para leer TODAS LAS LINEAS (restantes) del archivo 'demo.txt' de un solo tiro, podemos utilizar el metodo READLINES(). este nos retorna una lista cuyos elementos son lineas del archivo 'demo.txt'. OJO. Cada elemento incluye un '\n' o un espacio al final. Depende del cambio a cada renglon o si al terminar la linea se deja un espacio sin querer.
# todasLasLineas = fichero.readlines()
# print(todasLasLineas)

# Si primero invoco el metodo READLINE y luego el READLINES, va a imprimir la primera linea y luego procedera a imprimir en una lista las lineas RESTANTES.
# print(fichero.readline())
# print(fichero.readlines())

# 3. Por ultimo debemos cerrar el archivo.
fichero.close()




#MODO ESCRITURA
# El archivo 'demo.txt' originalmente tiene las siguientes 3 lineas:
#Esta es una acción de trabajo con archivos externos.
#También sirve como referencia de estudio.
#Y por último voy verificando cada paso en linea.

# Escribir en un archivo existente. Si lo abro en modo write 'w' lo que exista en el archivo anteriormente se perderá, ya que sobre-escribe lo nuevo que generemos.
# fichero = open("./Semana5/clase_archivos/demo.txt", "w", encoding="utf-8")
# fichero.write("Me he cargado todo lo que existia.\n") # Sobre-escribe este nuevo texto
# Podemos escribir varias lineas al mismo tiempo utilizando las listas e invocando el metodo WRITELINES.
# listaContendio = ["Dimas es el mejor youtuber.\n", "Me turboflipa su", " curso de Python.\n", "Adios muy buenas.\n"]
# fichero.writelines(listaContendio)
# fichero.close()
# El archivo 'demo.txt' quedo convertido en lo siguiente:
# Me he cargado todo lo que existia.
# Dimas es el mejor youtuber.
# Me turboflipa su curso de Python.
# Adios muy buenas.

#ALTERNATIVA. Evitar repetir escriber tantas veces '\n'
# fichero = open("./Semana5/clase_archivos/demo.txt", "w", encoding="utf-8")
# fichero.write("Me he cargado todo lo que existia.\n")
# listaContendio = ["Dimas es el mejor youtuber.", "Me turboflipa su curso de Python.", "Adios muy buenas."]
# # Incluir esta linea de codigo.
# listaContendio = list(map(lambda line: line + '\n', listaContendio))
# print(listaContendio)   # Para visualizar por pantalla que la anterior linea de codigo funciona adicionando el string '\n' a cada linea de texto o cada elemento de la lista.
# fichero.writelines(listaContendio)
# fichero.close()

#MODO ESCRITURA
# El archivo 'demo.txt' en este momento tiene las siguientes lineas:
# Me he cargado todo lo que existia.
# Dimas es el mejor youtuber.
# Me turboflipa su curso de Python.
# Adios muy buenas.

# Escribir en un archivo existente. Si lo abro en MODO APPEND 'a' va añadir contenido sin eliminar el existente.
# fichero = open("./Semana5/clase_archivos/demo.txt", "a", encoding="utf-8")
# fichero.write("\n\n\nEsto es una nueva linea.")   # Doy 3 saltos de linea. Al final no.
# fichero.close()
# El archivo 'demo.txt' quedo convertido en lo siguiente:
# Me he cargado todo lo que existia.
# Dimas es el mejor youtuber.
# Me turboflipa su curso de Python.
# Adios muy buenas.
# 1 espacio
# 2 espacio
# 3 espacio
# Esto es una nueva linea.




#MODO CREANDO
# Sirve para crear un nuevo archivo. Cuando usamos open en MODO CREATE, podemos escribir en el archivo tras crearlo pero no leer.
# fichero = open("./Semana5/clase_archivos/demo2.txt", "x", encoding="utf-8")
# fichero.write("Soy un archivo nuevooooo")
# fichero.close()
# Si intentamos crear un archivo que ya existe saltara una excepcion.


# MODO LECTURA VARIANTE. Metodo SEEK. Podemos controlar la posicion desde la cual empezamos a leer.
# fichero = open("./Semana5/clase_archivos/demo.txt", encoding="utf-8")
# fichero.seek(10)
# print("Estamos leyendo desde el decimo caracter: \n")
# print(fichero.read())
# fichero.close()

# MODO LECTURA Y ESCRITURA SIMULTANEA.
# fichero = open("./Semana5/clase_archivos/demo.txt", "r+", encoding="utf-8")
# lineas = fichero.readlines()
# print(lineas)
# fichero.write("\nLinea super nuevaaaaaa.")
# fichero.close()

#Ahora invierto las acciones.Primero escribo y luego leo
#Sucede que escribe la nueva linea al final como si fuera un append, pero la lectura de las lineas la realiza sin incluir la nueva linea. Como si estuviera primero leyendo y luego escribiendo.
""" fichero = open("./Semana5/clase_archivos/demo.txt", "r+", encoding="utf-8")
fichero.write("\nLinea RECONTRA super nuevaaaaaa.")
lineas = fichero.readlines()
print(lineas)
fichero.close() """

