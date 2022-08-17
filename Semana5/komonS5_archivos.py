import S5Komon as Red


#Aqui empieza el programa. Damos bienvenida y preguntamos nombre para buscar archivo.
Red.mostrar_bienvenida()
nombre = Red.obtener_nombre()

#Verificamos si el archivo existe
if Red.existe_archivo(nombre):
    #Pasamos funcion para leer el archivo existente
    (nombre, edad, estatura_m, estatura_cm, num_amigos, genero, n_telefonico, ciudad_vive) = Red.leer_archivo(nombre)
else:
    #En caso que el usuario NO exista, consultamos por sus datos
    (edad, estatura_m, estatura_cm, num_amigos, genero, n_telefonico, ciudad_vive) = Red.obtener_datos()

#En ambos casos, al llegar aquÃ­ ya conocemos los datos del usuario
print()
print("Muy bien,", nombre, ".Hasta el momento tenemos lo siguiente:")
Red.perfil_komon(nombre, edad, estatura_m, estatura_cm, num_amigos, genero, n_telefonico, ciudad_vive)
print("Gracias por información suministrada. Disfruta KOMON")
print("----------------------------------------------------------------------------")
print()
menu = True
while menu:
    opcion_menu = Red.opcion_menu_principal()   #aqui va el menu principal
    
    if opcion_menu == 1:
        menu_perfil = True
        while menu_perfil:
            opcion_menu_perfil = Red.opcion_perfil()   #aqui va el menu de perfil
            
            if opcion_menu_perfil == 1:
                nombre = Red.nuevo_nombre()
            elif opcion_menu_perfil == 2:
                edad = Red.nueva_edad()
            elif opcion_menu_perfil == 3:
                (estatura_m, estatura_cm) = Red.nueva_estatura()
            elif opcion_menu_perfil == 4:
                num_amigos = Red.nuevos_amigos()
            elif opcion_menu_perfil == 5:
                genero = Red.nuevo_genero()
            elif opcion_menu_perfil == 6:
                n_telefonico = Red.nuevo_telefono()
            elif opcion_menu_perfil == 7:
                ciudad_vive = Red.nueva_ciudad()
            elif opcion_menu_perfil == 8:
                Red.perfil_komon(nombre, edad, estatura_m, estatura_cm, num_amigos, genero, n_telefonico, ciudad_vive)
            else:
                print()
                print("A tus ordenes!", nombre)
                menu_perfil = False
                print()
    
    elif opcion_menu == 2:
        Red.perfil_komon(nombre, edad, estatura_m, estatura_cm, num_amigos, genero, n_telefonico, ciudad_vive)
        print()

    elif opcion_menu == 3:
        Red.mens_publico(nombre)
        print()
    
    elif opcion_menu == 4:
        Red.mens_privado(nombre)
        print()
    
    elif opcion_menu == 5:
        Red.escribir_archivo(nombre, edad, estatura_m, estatura_cm, num_amigos, genero, n_telefonico, ciudad_vive)
        menu = False
        Red.cambiar_usuario()
        print()
    else:
        Red.escribir_archivo(nombre, edad, estatura_m, estatura_cm, num_amigos, genero, n_telefonico, ciudad_vive)
        menu = False  
        print()
        print("Gracias ",nombre," por usar KOMON. ¡Hasta pronto!")
        print()