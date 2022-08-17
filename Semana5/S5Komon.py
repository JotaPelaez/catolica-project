#El modulo 'os' nos permite consultar si un archivo existe.
import os


def mostrar_bienvenida():
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

def obtener_nombre():
    ingreso = input("Para empezar, dime como te llamas?: ")
    nombre = ingreso.title()
    print()
    print("Hola ", nombre, "... Bienvenido a KOMON")
    print()
    return nombre

def existe_archivo(name):
    return os.path.isfile("./Semana5/usuarios/"+name + ".user")

def leer_archivo (name):
    print("Leyendo datos de usuario", name, "desde archivo.")
    archivo_usuario = open("./Semana5/usuarios/"+name+".user", "r")
    n = archivo_usuario.readline().replace("\n", "")  # n = n[0:len(n)-1] o n = n.rstrip()  
    e = int(archivo_usuario.readline().replace("\n", ""))
    estatura = float(archivo_usuario.readline().replace("\n", ""))
    em = int(estatura)
    ec = int((estatura - em)*100)
    na = int(archivo_usuario.readline().replace("\n", ""))
    ge = archivo_usuario.readline().replace("\n", "")
    ntelf = archivo_usuario.readline().replace("\n", "")
    cvi = archivo_usuario.readline().replace("\n", "")
    archivo_usuario.close()
    return (n, e, em, ec, na, ge, ntelf, cvi)
    
def obtener_edad ():
    agno = int(input("* Para preparar tu 'perfil',dime en que año naciste?: "))
    return 2022-agno-1
    
def obtener_estatura ():
    estatura = float(input("* Pefecto! Ahora dime ¿Cuánto mides? Dámelo en metros: "))
    metros = int(estatura)
    centimetros = int( (estatura - metros)*100 )
    return(metros,centimetros)
    
def obtener_num_amigos():
    amigos = int(input("* Muy bien. Entonces, cuéntame cuántos amigos tienes: "))
    return amigos

def obtener_genero():
    genero = input("* Vaya numero! Ahora indica género (M=Masculino o F=Femenino): ")
    genero = genero.upper()
    while genero != 'M' and genero != 'F':
        genero = input("Revisa tu seleccion (M=Masculino o F=Femenino): ")
    return genero

def obtener_telefono():
    n_telefonico = input("* Perfecto. Por favor ingresa tu número telefónico: ")
    return n_telefonico

def obtener_ciudad():
    city_life = input("* Finalmente, dime en que ciudad vives?: ")
    return city_life

def obtener_datos():
    e = obtener_edad()
    (em, ec) = obtener_estatura()
    na = obtener_num_amigos()
    ge = obtener_genero()
    ntelf = obtener_telefono()
    cvi = obtener_ciudad()
    return(e, em, ec, na, ge, ntelf, cvi)

def perfil_komon(nombre, edad, estatura_m, estatura_cm, num_amigos, genero, n_telefonico, ciudad_vive):
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

def opcion_menu_principal():
    print("---> M E N U   P R I N C I P A L <---")
    print("1. Actualizar tu perfil")
    print("2. Mostrar tu perfil")
    print("3. Escribir un mensaje publico")
    print("4. Escribir mensaje privado")
    print("5. Cambiar de usuario")
    print("6. Salir")
    print()
    option_main_menu=int(input("Que deseas hacer ahora?. Selecciona una opcion: "))
    while option_main_menu < 1 or option_main_menu > 6:
        print("Opcion 'NO' identificada. Inténtalo otra vez.")
        option_main_menu = int(input("Rectifica la opción escogida: "))
    return option_main_menu
    
def cambiar_usuario():
    print()
    ingreso = input("Digite el nombre del usuario: ")
    nombre = ingreso.title()
    if existe_archivo(nombre):
        (nombre, edad, estatura_m, estatura_cm, num_amigos, genero, n_telefonico, ciudad_vive) = leer_archivo(nombre)
        perfil_komon(nombre, edad, estatura_m, estatura_cm, num_amigos, genero, n_telefonico, ciudad_vive)
        print("Datos KOMON almacenados de", nombre, "hasta el momento.")
        print("----------------------------------------------------------------------------")
        print()
        menu = True
        while menu:
            opcion_menu = opcion_menu_principal()   #aqui va el menu principal
            
            if opcion_menu == 1:
                menu_perfil = True
                while menu_perfil:
                    opcion_menu_perfil = opcion_perfil()   #aqui va el menu de perfil
            
                    if opcion_menu_perfil == 1:
                        nombre = nuevo_nombre()
                    elif opcion_menu_perfil == 2:
                        edad = nueva_edad()
                    elif opcion_menu_perfil == 3:
                        (estatura_m, estatura_cm) = nueva_estatura()
                    elif opcion_menu_perfil == 4:
                        num_amigos = nuevos_amigos()
                    elif opcion_menu_perfil == 5:
                        genero = nuevo_genero()
                    elif opcion_menu_perfil == 6:
                        n_telefonico = nuevo_telefono()
                    elif opcion_menu_perfil == 7:
                        ciudad_vive = nueva_ciudad()
                    elif opcion_menu_perfil == 8:
                        perfil_komon(nombre, edad, estatura_m, estatura_cm, num_amigos, genero, n_telefonico, ciudad_vive)
                    else:
                        print()
                        print("A tus ordenes!", nombre)
                        menu_perfil = False
                        print()
            
            elif opcion_menu == 2:
                perfil_komon(nombre, edad, estatura_m, estatura_cm, num_amigos, genero, n_telefonico, ciudad_vive)
                print()

            elif opcion_menu == 3:
                mens_publico(nombre)
                print()
            
            elif opcion_menu == 4:
                mens_privado(nombre)
                print()
            elif opcion_menu == 5:
                escribir_archivo(nombre, edad, estatura_m, estatura_cm, num_amigos, genero, n_telefonico, ciudad_vive)
                menu = False
                cambiar_usuario()
                print()
            else:
                escribir_archivo(nombre, edad, estatura_m, estatura_cm, num_amigos, genero, n_telefonico, ciudad_vive)
                menu = False
                print()
                print("Gracias ",nombre," por usar KOMON. ¡Hasta pronto!")
                print()
                       
        
    else:
        print()
        print("** NO EXISTE. No se puede cambiar a ese usuario **")
        menu = False
        print()
    
def opcion_perfil():
    print()
    print("---> P E R F I L <---")
    print("1. Nombre")
    print("2. Edad")
    print("3. Estatura")
    print("4. Amigos")
    print("5. Genero")
    print("6. Telefono")
    print("7. Ciudad")
    print("8. Mostrar tu perfil")
    print("9. Salir")
    print()
    option_menu_profile = int(input("Selecciona una opcion: "))
    while option_menu_profile < 1 or option_menu_profile > 9:
        print("Opcion equivocada. Vamos de nuevo!.")
        option_menu_profile = int(input("Rectifica la opción escogida: "))
    return option_menu_profile
    
def nuevo_nombre():
    print()
    continuar = True
    while continuar:
        print("**ATENCION** Cambiar tu nombre--> Crea un nuevo usuario")
        print()
        nombre = input("* Escribe nuevo NOMBRE: ")
        if existe_archivo(nombre):
            print("Ya existe este nombre")
        else:
            print("** Tu NOMBRE ha sido modificado **")
            continuar = False
    return nombre
    
def nueva_edad():
    print()
    edad=int(input("* Escribe nueva EDAD: "))
    print("** Tu EDAD ha sido modificada **")
    return edad 
   
def nueva_estatura():
    print()
    estatura=float(input("* Escribe nueva ESTATURA: "))
    metros = int(estatura)
    centimetros = int( (estatura - metros)*100 )
    print("** Tu ESTATURA ha sido modificada **")
    return (metros, centimetros)

def nuevos_amigos():
    print()
    new_friend = input("* Escribe nueva cantidad de AMIGOS: ")
    print("** Tu cantidad de AMIGOS ha sido modificada **")
    return new_friend 

def nuevo_genero():
    print()
    new_sex = input("* Escribe tu nuevo GENERO: ")
    new_sex = new_sex.upper()
    print("** Tu GENERO ha sido modificado **")
    return new_sex 

def nuevo_telefono():
    print()
    new_phone = input("* Escribe tu nuevo numero TELEFONICO: ")
    print("** Tu número TELEFONICO ha sido modificado **")
    return new_phone 

def nueva_ciudad():
    print()
    new_city = input("* Escribe tu nueva CIUDAD: ")
    print("** Tu CIUDAD ha sido modificada **")
    return new_city 

def mens_publico(name):
    print()
    mensaje = (input("* Escribe tu mensaje: "))
    print()
    print("------------------------------------------------------------------------")
    print(">>>>",name, "dice:", mensaje,"<<<<")
    print("------------------------------------------------------------------------")
    print()
    continuar = True
    while continuar:
        escribir_mensaje = (input("Deseas escribir otro mensaje? (S/N) "))
        if escribir_mensaje == "S" or escribir_mensaje == "s"or escribir_mensaje == "":
            print()
            mensaje = (input("* Escribe tu mensaje: "))
            print("------------------------------------------------------------------------")
            print()
            print(">>>>",name, "dice:", mensaje,"<<<<")
            print("------------------------------------------------------------------------")
            print()

        elif escribir_mensaje == "N" or escribir_mensaje == "n":
            continuar=False
            print()

def mens_privado(name):
    print()
    mensaje = (input("* Mensaje privado: "))
    nom_amigo = (input("* Amigo que recibira tu mensaje: "))
    print()
    print("------------------------------------------------------------------------")
    print(">>>>",name, "dice ... @"+nom_amigo,mensaje,"<<<<")
    print("------------------------------------------------------------------------")
    print()
    continuar = True
    while continuar:
            escribir_mensaje = (input("Deseas escribir otro mensaje? (S/N) "))
            if escribir_mensaje == "S" or escribir_mensaje == "s"or escribir_mensaje == "":
                print()
                mensaje = (input("* Mensaje privado: "))
                nom_amigo = (input("* Amigo que recibira tu mensaje: "))
                print()
                print("------------------------------------------------------------------------")
                print(">>>>",name, "dice ... @"+nom_amigo,mensaje,"<<<<")
                print("------------------------------------------------------------------------")
                print()

            elif escribir_mensaje == "N" or escribir_mensaje == "n":
                continuar=False
                print()

def escribir_archivo (nombre, edad, estatura_m, estatura_cm, num_amigos, genero, n_telefonico, ciudad_vive):
    print("Has decidido salir. Guardando perfil en", nombre + ".user")
    archivo_usuario = open("./Semana5/usuarios/"+nombre + ".user", "w")
    archivo_usuario.write(nombre + "\n")      
    archivo_usuario.write(str(edad) + "\n")
    archivo_usuario.write(str(estatura_m + estatura_cm/100) + "\n")
    archivo_usuario.write(str(num_amigos) + "\n")
    archivo_usuario.write(genero + "\n")
    archivo_usuario.write(n_telefonico + "\n")
    archivo_usuario.write(ciudad_vive + "\n")
    archivo_usuario.close()
    print("Archivo", nombre + ".user", "guardado")
    