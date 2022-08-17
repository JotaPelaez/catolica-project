# 1. El else esta mal escrito. No funciona
nombre="Danilo"
continuar=True
# while continuar:
#     escribir = str(input("¿Deseas escribir un mensaje? (S/N) "))
#     if escribir=="S" or escribir=="s" or escribir=="":
#         mensaje = input("¿Qué piensas hoy? ")
#         print(nombre, "dice:", mensaje)
#     else escribir=="N" or escribir=="n":      
#         continuar = False


# 2.Funciona con S y N, pero con otra letra vuelve a preguntar.Despues del 2do "" se termina el programa. No funciona
# while continuar:
#     escribir = str(input("¿Deseas escribir un mensaje? (S/N) "))
#     if escribir=="S" or escribir=="s" or escribir=="":
#         mensaje = input("¿Qué piensas hoy? ")
#     print(nombre, "dice:", mensaje)
#     if escribir=="N" or escribir=="n" or escribir=="":
#         continuar = False    


# 3.Similar al anterior. Se le quita el 2do "" para que solo aplique en la pregunta del S. No funciona
# while continuar:
#     escribir = str(input("¿Deseas escribir un mensaje? (S/N) "))
#     if escribir=="S" or escribir=="s" or escribir=="":
#         mensaje = input("¿Qué piensas hoy? ")
#         print(nombre, "dice:", mensaje)
#     if escribir=="N" or escribir=="n":
#         continuar = False      


# 4.Se queda infinitamente haciendo la misma pregunta con distitas letras, incluida la N. Cuando escribe S se recibe el mensaje y vuelve a preguntar. No funciona
# while continuar:
#     escribir = str(input("¿Deseas escribir un mensaje? (S/N) "))
#     if escribir=="S" or escribir=="s" or escribir=="":
#         mensaje = input("¿Qué piensas hoy? ")
#         print(nombre, "dice:", mensaje)
#         continuar = False 


# 5.Con S recibe el mensaje y vuelve a preguntar. Con letras distintas incluida la N se termina el programa. No funciona
# while continuar:
#     escribir = str(input("¿Deseas escribir un mensaje? (S/N) "))
#     if escribir=="S" or escribir=="s" or escribir=="":
#         mensaje = input("¿Qué piensas hoy? ")
#         print(nombre, "dice:", mensaje)
#     if not(escribir=="S" or escribir=="s" or escribir==""):
#         continuar = False

# 6.Este funciona bien..... Con S recibe mensaje, con N se sale y con otra letra sigue haciendo la pregunta
while continuar:
    escribir = str(input("¿Deseas escribir un mensaje? (S/N) "))
    if escribir=="S" or escribir=="s" or escribir=="":
        mensaje = input("¿Qué piensas hoy? ")
        print(nombre, "dice:", mensaje)
    elif escribir=="N" or escribir=="n":
        continuar = False


# 1. Solo con 0 se puede salir. De resto con las opciones las ejecuta y sigue la misma pregunta. Funciona
opcion = -1
while opcion != 0:
    opcion=int(input("Elija opcion 1, 2 o 0 (salir):"))
    if opcion == 1:
        print("Ejecutamos la opcion 1")
    elif opcion == 2:
        print("Ejecutamos la opcion 2")
    elif opcion == 0:
        print("Has decidido salir.")


# 2. Nunca entra porque 0 ES IGUAL A 0. No funciona
# opcion = 0
# while opcion != 0:
#     opcion=int(input("Elija opcion 1, 2 o 0 (salir):"))
#     if opcion == 1:
#         print("Ejecutamos la opcion 1")
#     elif opcion == 2:
#         print("Ejecutamos la opcion 2")
#     elif opcion == 0:
#         print("Has decidido salir.")


# 3. Ejecuta cada opcion y vuelve a preguntar. Con 0 sale del sistema y termina.Funciona.
opcion = -1
while opcion != 0:
    opcion=int(input("Elija opcion 1, 2 o 0 (salir):"))
    if opcion == 0:
        print("Has decidido salir")
    if opcion == 1:
        print("Ejecutamos la accion 1")
    elif opcion == 2:
        print("Ejecutamos la accion 2")


# 4. Ejecuta cada opcion y termina con 0 y con otro cualquier numero diferente a 1 y 2. No Funciona.
# opcion = -1
# while opcion != 0:
#     opcion=int(input("Elija opcion 1, 2 o 0 (salir):"))
#     if opcion == 1:
#         print("Ejecutamos la opcion 1")
#     elif opcion == 2:
#         print("Ejecutamos la opcion 2")
#     else:
#         print("Has decidido salir.")
#         opcion = 0


# 5. Ejecuta cada opcion y termina con 0 y con otro cualquier numero diferente a 1 y 2 sigue pidiendo la opcion. Funciona.
opcion = -1
while opcion != 0:
    opcion=int(input("Elija opcion 1, 2 o 0 (salir):"))
    if opcion != 0:
        if opcion == 1:
            print("Ejecutamos la opcion 1")
        elif opcion == 2:
            print("Ejecutamos la opcion 2")
    else:
        print("Has decidido salir.")


# 6. Con 0 ejecuta pero no termina. Vuelve a preguntar. Con las otras opciones si termina. No Funciona.
# opcion = 0
# while opcion == 0:
#     opcion=int(input("Elija opcion 1, 2 o 0 (salir):"))
#     if opcion == 1:
#         print("Ejecutamos la opcion 1")
#     elif opcion == 2:
#         print("Ejecutamos la opcion 2")
#     elif opcion == 0:
#         print("Has decidido salir.")



