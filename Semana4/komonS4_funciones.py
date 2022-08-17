import S4Komon as Red


Red.mostrar_bienvenida()
(nombre, edad, estatura_m, estatura_cm, num_amigos, genero, n_telefonico, ciudad_vive)=Red.obtener_datos()
print()
print("Muy bien,", nombre, ". Hasta el momento tenemos lo siguiente:")
Red.perfil_komon(nombre, edad, estatura_m, estatura_cm, num_amigos, genero, n_telefonico, ciudad_vive)
print()
print("Gracias por la información. Disfruta KOMON")
print()
menu=True
while menu:
    opcion_menu=Red.opcion_menu_principal()   #aqui va el menu principal
    if opcion_menu==1:
        menu_perfil=True
        while menu_perfil:
            opcion_menu_perfil=Red.opcion_perfil()   #aqui va el menu de perfil
            if opcion_menu_perfil==1:
                nombre=Red.nuevo_nombre()
            elif opcion_menu_perfil==2:
                edad=Red.nueva_edad()
            elif opcion_menu_perfil==3:
                (estatura_m, estatura_cm)=Red.nueva_estatura()
            elif opcion_menu_perfil==4:
                Red.perfil_komon(nombre, edad, estatura_m, estatura_cm, num_amigos, genero, n_telefonico, ciudad_vive)
            else:
                print()
                print("A tus ordenes!", nombre)
                menu_perfil=False
                print()
    elif opcion_menu==2:
        Red.perfil_komon(nombre, edad, estatura_m, estatura_cm, num_amigos, genero, n_telefonico, ciudad_vive)
        print()

    elif opcion_menu==3:
        Red.mens_publico(nombre)
        print()
    elif opcion_menu==4:
        Red.mens_privado(nombre)
        print()
    else:
        print()
        print("Gracias ",nombre," por usar KOMON. ¡Hasta pronto!")
        menu=False
        print()