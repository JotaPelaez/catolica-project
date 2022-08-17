print()
print("Bienvenido a ... ")
print("""
/**  **                                        
/** **    ******  **********   ******  ******* 
/****    **////**//**//**//** **////**//**///**
/**/**  /**   /** /** /** /**/**   /** /**  /**
/**//** /**   /** /** /** /**/**   /** /**  /**
/** //**//******  *** /** /**//******  ***  /**
//   //  //////  ///  //  //  //////  ///   // 
""")
print()
nombre = input("Para empezar, dime como te llamas?: ")
print()
print("Hola ", nombre, "... Bienvenido a KOMON")
print()
agno = int(input("* Para preparar tu 'perfil',dime en que año naciste?: "))
edad = 2022-agno-1
estatura = float(input("* Pefecto! Ahora dime ¿Cuánto mides? Dámelo en metros: "))
estatura_m = int(estatura)
estatura_cm = int( (estatura - estatura_m)*100 )
num_amigos = int(input("* Muy bien. Entonces, cuéntame cuántos amigos tienes: "))
genero = input("* Vaya numero! Ahora indica tu género (Masculino o Femenino): ")
n_telefonico = input("* Perfecto. Por favor ingresa tu número telefónico: ")
ciudad_vive = input("* Finalmente, dime en que ciudad vives?: ")
print()
print("Muy bien,", nombre, ". Hasta el momento tenemos lo siguiente:")
print()
print("----------------------------------------------------------------------------")
print("****************************--->PERFIL KOMON<---****************************")
print("----------------------------------------------------------------------------")
print("NOMBRE:  --->", nombre)
print("EDAD:  --->  ", edad, "años")
print("ESTATURA:  --->", estatura_m, "metro y", estatura_cm, "centímetros")
print("AMIGOS:  --->", num_amigos)
print("GENERO:  --->", genero)
print("NUMERO TELEFONICO:  --->", n_telefonico)
print("CIUDAD DONDE RESIDES:  --->  ", ciudad_vive)
print("----------------------------------------------------------------------------")

print()
print("Gracias por la información. Disfruta KOMON")
print()
menu=True
while menu:
    print("---> M E N U <---")
    print("1. Actualizar tu perfil")
    print("2. Mostrar tu perfil")
    print("3. Escribir un mensaje")
    print("4. Salir")
    print()
    opcion_menu=int(input("Que deseas hacer ahora?. Selecciona una opcion: "))
    if opcion_menu==1:
        menu_perfil=True
        while menu_perfil:
            print()
            print("---> P E R F I L <---")
            print("1. Nombre")
            print("2. Edad")
            print("3. Estatura")
            print("4. Salir")
            print()
            opcion_menu_perfil=int(input("Selecciona una opcion: "))
            if opcion_menu_perfil==1:
                print()
                nombre=input("* Escribe nuevo NOMBRE: ")
                
                print("** Tu NOMBRE ha sido modificado **")
            elif opcion_menu_perfil==2:
                print()
                edad=int(input("* Escribe nueva EDAD: "))
                
                print("** Tu EDAD ha sido modificada **")
            elif opcion_menu_perfil==3:
                print()
                estatura=float(input("* Escribe nueva ESTATURA: "))
                estatura_m = int(estatura)
                estatura_cm = int( (estatura - estatura_m)*100 )
                print("** Tu ESTATURA ha sido modificada **")
            else:
                print()
                print("A tus ordenes!", nombre)
                menu_perfil=False
                print()
    elif opcion_menu==2:
        print()
        print("----------------------------------------------------------------------------")
        print("****************************--->PERFIL KOMON<---****************************")
        print("----------------------------------------------------------------------------")
        print("NOMBRE:  --->", nombre)
        print("EDAD:  --->  ", edad, "años")
        print("ESTATURA:  --->", estatura_m, "metro y", estatura_cm, "centímetros")
        print("AMIGOS:  --->", num_amigos)
        print("GENERO:  --->", genero)
        print("NUMERO TELEFONICO:  --->", n_telefonico)
        print("CIUDAD DONDE RESIDES:  --->  ", ciudad_vive)
        print("----------------------------------------------------------------------------")
        print()
        print()

    elif opcion_menu==3:
        mensaje = (input("* Escribe tu mensaje: "))
        print()
        print("------------------------------------------------------------------------")
        print(">>>>",nombre, "dice:", mensaje,"<<<<")
        print("------------------------------------------------------------------------")
        print()
        continuar = True
        while continuar:
            escribir_mensaje = str(input("Deseas escribir otro mensaje? (S/N) "))
            if escribir_mensaje == "S" or escribir_mensaje == "s"or escribir_mensaje == "":
                mensaje = (input("* Escribe tu mensaje: "))
                print("------------------------------------------------------------------------")
                print(">>>>",nombre, "dice:", mensaje,"<<<<")
                print("------------------------------------------------------------------------")
                print()

            elif escribir_mensaje == "N" or escribir_mensaje == "n":
                continuar=False
                print()
                print()
                
    else:
        print()
        print("Gracias ",nombre," por usar KOMON. ¡Hasta pronto!")
        menu=False
        print()

#Usaremos una variable bool para indicar si el usuario desea continuar
#utilizando el programa o no

#Este ciclo se mantiene en ejecuciÃ³n hasta que el usuario desee salir

#Solicitamos opciÃ³n al usuario

#Vamos a aceptar que el usuario ingrese un mensaje cuando escriban "S", "s", o nada
    
#En caso que sea otra respuesta, vamos a decidir salir.
#AsÃ­, en la siguiente iteraciÃ³n el ciclo terminarÃ¡
    
    
#Mensaje de salida, una vez que el ciclo ha terminado.
# print()
# print("Gracias ",nombre," por usar KOMON. ¡Hasta pronto!")
# print()


#Ahora puedes escribir mensajes todas las veces que quieras.
#Observa que hemos utilizado un ciclo while que permite repetir la acciÃ³n de preguntar por un mensajes
#hasta que el usuario escribe algo distino de "S".

#Pero las redes sociales pueden ejecutar mÃ¡s acciones que solamente enviar mensajes.

#Te proponemos los siguientes desafÃ­os:
#1. Este programa termina cada vez que el valor de 'escribir_mensaje' es distinto a "S" o a "s".
#   Modifique el programa para que el programa termine UNICAMENTE cuando se ingresa "N" o "n".
#   En caso que se ingrese algo distinto, debe volver a solicitar una opciÃ³n al usuario.
#
#2. Modifica este menÃº para que le permita el usuario realizar mÃ¡s de una acciÃ³n.
#   Por ejemplo, puedes agregar una acciÃ³n que permita al usuario modificar su nombre.