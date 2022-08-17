
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
    nombre = input("Para empezar, dime como te llamas?: ")
    print()
    print("Hola ", nombre, "... Bienvenido a KOMON")
    print()
    return nombre
    
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
    genero = input("* Vaya numero! Ahora indica tu género (Masculino o Femenino): ")
    return genero

def obtener_telefono():
    n_telefonico = input("* Perfecto. Por favor ingresa tu número telefónico: ")
    return n_telefonico

def obtener_ciudad():
    city_life = input("* Finalmente, dime en que ciudad vives?: ")
    return city_life

def obtener_datos():
    n = obtener_nombre()
    e = obtener_edad()
    (em, ec) = obtener_estatura()
    na = obtener_num_amigos()
    ge = obtener_genero()
    ntelf = obtener_telefono()
    cvi = obtener_ciudad()
    return(n, e, em, ec, na, ge, ntelf, cvi)

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
    print("5. Salir")
    print()
    option_main_menu=int(input("Que deseas hacer ahora?. Selecciona una opcion: "))
    while option_main_menu < 1 or option_main_menu > 5:
        print("Opcion 'NO' identificada. Inténtalo otra vez.")
        option_main_menu = int(input("Rectifica la opción escogida: "))
    return option_main_menu
    
def opcion_perfil():
    print()
    print("---> P E R F I L <---")
    print("1. Nombre")
    print("2. Edad")
    print("3. Estatura")
    print("4. Mostrar tu perfil")
    print("5. Salir")
    print()
    option_menu_profile=int(input("Selecciona una opcion: "))
    while option_menu_profile < 1 or option_menu_profile > 5:
        print("Opcion equivocada. Vamos de nuevo!.")
        option_menu_profile = int(input("Rectifica la opción escogida: "))
    return option_menu_profile
    
def nuevo_nombre():
    print()
    new_name=input("* Escribe nuevo NOMBRE: ")
    print("** Tu NOMBRE ha sido modificado **")
    return new_name
    
def nueva_edad():
    print()
    new_age=int(input("* Escribe nueva EDAD: "))
    print("** Tu EDAD ha sido modificada **")
    return new_age 
   
def nueva_estatura():
    print()
    estatura=float(input("* Escribe nueva ESTATURA: "))
    metros = int(estatura)
    centimetros = int( (estatura - metros)*100 )
    print("** Tu ESTATURA ha sido modificada **")
    return (metros, centimetros)

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

