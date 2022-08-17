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
    print()
    print("Leyendo datos de usuario", name, "desde archivo.")
    archivo_usuario = open("./Semana5/usuarios/"+name+".user", "r")
    n = archivo_usuario.readline().rstrip()  
    e = int(archivo_usuario.readline())
    estatura = float(archivo_usuario.readline())
    em = int(estatura)
    ec = int((estatura - em)*100)
    la = archivo_usuario.readline().rstrip().split(',')
    ge = archivo_usuario.readline().rstrip()
    ntelf = archivo_usuario.readline().rstrip()
    cvi = archivo_usuario.readline().rstrip()
    estado = archivo_usuario.readline().rstrip()
    #Lee el 'muro'. Esto es, todos los mensajes que han sido publicados en el timeline del usuario.
    muro = []
    mensaje = archivo_usuario.readline().rstrip()
    while mensaje != "":
        muro.append(mensaje)
        mensaje = archivo_usuario.readline().rstrip()
    #Una vez que hemos leido los datos del usuario no debemos olvidar cerrar el archivo
    archivo_usuario.close()
    return (n, e, em, ec, la, ge, ntelf, cvi, estado, muro)
    
def obtener_edad ():
    agno = int(input("* Para preparar tu 'perfil',dime en que año naciste?: "))
    return 2022-agno-1
    
def obtener_estatura ():
    estatura = float(input("* Pefecto! Ahora dime ¿Cuánto mides? Dámelo en metros: "))
    metros = int(estatura)
    centimetros = int( (estatura - metros)*100 )
    return(metros,centimetros)
    
def obtener_lista_amigos():
    amigos = []
    linea = input("Lista los nombres de tus amigos, separados por una ',': ")
    if ',' in linea:
        amigos = linea.split(",")
        return amigos
    else:
        amigos.append(linea)
        return amigos  
    
def obtener_genero():
    genero = input("* Vaya numero! Ahora indica género (M=Masculino o F=Femenino): ")
    genero = genero.upper()
    while genero != 'M' and genero != 'F':
        genero = input("Revisa tu seleccion (M=Masculino o F=Femenino): ")
    if genero == 'M':
        return 'Masculino'
    elif genero == 'F':
        return 'Femenino'
    
def obtener_telefono():
    n_telefonico = input("* Perfecto. Por favor ingresa tu número telefónico: ")
    return n_telefonico

def obtener_ciudad():
    city_life = input("* Finalmente, dime en que ciudad vives?: ")
    return city_life

def obtener_datos():
    e = obtener_edad()
    (em, ec) = obtener_estatura()
    la = obtener_lista_amigos()
    ge = obtener_genero()
    ntelf = obtener_telefono()
    cvi = obtener_ciudad()
    return(e, em, ec, la, ge, ntelf, cvi)

def perfil_komon(nombre, edad, estatura_m, estatura_cm, list_amigos, genero, n_telefonico, ciudad_vive):
    print("----------------------------------------------------------------------------")
    print("****************************--->PERFIL KOMON<---****************************")
    print("----------------------------------------------------------------------------")
    print("NOMBRE:  --->", nombre)
    print("EDAD:  --->  ", edad, "años")
    print("ESTATURA:  --->", estatura_m, "metro y", estatura_cm, "centímetros")
    print(f"NOMBRE AMIGOS ({len(list_amigos)}):  --->", list_amigos)
    print("GENERO:  --->", genero)
    print("NUMERO TELEFONICO:  --->", n_telefonico)
    print("CIUDAD DONDE RESIDES:  --->", ciudad_vive)
    print("----------------------------------------------------------------------------")
    
def mostrar_mensaje(origen, mensaje):
    print()
    print("----------------------------------------------------------------------------")
    print(origen+" escribio: ", mensaje)
    print("----------------------------------------------------------------------------")
    
def opcion_menu_principal():
    print()
    print("---> M E N U   P R I N C I P A L <---")
    print("1. Actualizar tu perfil")
    print("2. Mostrar tu perfil")
    print("3. Escribir un mensaje publico")
    print("4. Escribir mensaje privado")
    print("5. Mostrar mi muro")
    print("6. Mostrar ultimos estados amigos")
    print("7. Cambiar de usuario")
    print("8. Salir")
    print()
    option_main_menu=int(input("Que deseas hacer ahora?. Selecciona una opcion: "))
    while option_main_menu < 1 or option_main_menu > 8:
        print("Opcion 'NO' identificada. Inténtalo otra vez.")
        option_main_menu = int(input("Rectifica la opción escogida: "))
    return option_main_menu
    
def cambiar_usuario():
    print()
    ingreso = input(">>·Digite el nombre del usuario: ")
    nombre = ingreso.title()
    if existe_archivo(nombre):
        (nombre, edad, estatura_m, estatura_cm, list_amigos, genero, n_telefonico, ciudad_vive, estado, muro) = leer_archivo(nombre)
        perfil_komon(nombre, edad, estatura_m, estatura_cm, list_amigos, genero, n_telefonico, ciudad_vive)
        print("===========Datos KOMON almacenados de", nombre, "hasta el momento.==========")
        print("----------------------------------------------------------------------------")
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
                        list_amigos = list_amigos + nuevos_amigos()
                    elif opcion_menu_perfil == 5:
                        genero = nuevo_genero()
                    elif opcion_menu_perfil == 6:
                        n_telefonico = nuevo_telefono()
                    elif opcion_menu_perfil == 7:
                        ciudad_vive = nueva_ciudad()
                    elif opcion_menu_perfil == 8:
                        perfil_komon(nombre, edad, estatura_m, estatura_cm, list_amigos, genero, n_telefonico, ciudad_vive)
                    else:
                        print()
                        print("A tus ordenes!", nombre)
                        menu_perfil = False
                        print()
                        
            elif opcion_menu == 2:
                perfil_komon(nombre, edad, estatura_m, estatura_cm, list_amigos, genero, n_telefonico, ciudad_vive)
                print()
                
            elif opcion_menu == 3:
                estado = obtener_mensaje()
                publicar_mensaje(nombre, list_amigos, estado, muro)
                print()
                                            
            elif opcion_menu == 4:
                mens_privado(nombre)
                print()
                            
            elif opcion_menu == 5:
                mostrar_muro(muro)
                print()
            
            elif opcion_menu == 6:
                ultimos_estados(list_amigos)
                print()
                            
            elif opcion_menu == 7:
                escribir_archivo(nombre, edad, estatura_m, estatura_cm, list_amigos, genero, n_telefonico, ciudad_vive, estado, muro)
                menu = False
                cambiar_usuario()
                print()
                
            else:
                escribir_archivo(nombre, edad, estatura_m, estatura_cm, list_amigos, genero, n_telefonico, ciudad_vive, estado, muro)
                print()
                menu = False
                print("Gracias ",nombre," por usar KOMON. ¡Hasta pronto!")
                
        
    else:
        print("** NO EXISTE. No se puede cambiar a ese usuario **")
        menu = False
        
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
    new_amigos = []
    new_linea = input("Indica nuevos nombres de amigos, separados por una ',': ")
    if ',' in new_linea:
        new_amigos = new_linea.split(",")
        print("** Tus nuevos AMIGOS han sido adicionados **")
        return new_amigos
    else:
        new_amigos.append(new_linea)
        print("** Tu nuevo AMIGO(A) ha sido adicionado(a) **")
        return new_amigos 
    
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

#Muestra los mensajes recibidos
def mostrar_muro(muro):
    print()
    print("--------------------------- MURO ("+str(len(muro))+" mensajes) -------------------------")
    for mensaje in muro:
        print(mensaje)
    print("----------------------------------------------------------------------------") 

#Se captura el mensaje publico para tu comunidad de amigos
def obtener_mensaje():
    mensaje = (input("* Escribe tu mensaje: "))
    return mensaje

#Publica un mensaje en el timeline personal y en el de los amigos
def publicar_mensaje(name, amigos, mensaje, muro):
    print("------------------------------------------------------------------------")
    print(">>>>",name, "dice:", mensaje,"<<<<")
    print("------------------------------------------------------------------------")
    #Agrega el mensaje al final del timeline local
    muro.append(mensaje)
    #Agrega, al final del archivo de cada amigo, el mensaje publicado
    for amigo in amigos:
        if existe_archivo(amigo):
            archivo = open("./Semana5/usuarios/"+amigo+".user","a")
            archivo.write(name+":"+mensaje+"\n")
            archivo.close()
    
def mens_privado(name):
    print()
    mensaje_priv = (input("* Mensaje privado: "))
    nom_amigo = (input("* Amigo que recibira tu mensaje: "))
    print()
    print("------------------------------------------------------------------------")
    print(">>>>",name, "dice ... @"+nom_amigo,mensaje_priv,"<<<<")
    print("------------------------------------------------------------------------")
    print()
    continuar = True
    while continuar:
            escribir_mensaje = (input("Deseas escribir otro mensaje? (S/N) "))
            if escribir_mensaje == "S" or escribir_mensaje == "s"or escribir_mensaje == "":
                print()
                mensaje_priv = (input("* Mensaje privado: "))
                nom_amigo = (input("* Amigo que recibira tu mensaje: "))
                print()
                print("------------------------------------------------------------------------")
                print(">>>>",name, "dice ... @"+nom_amigo,mensaje_priv,"<<<<")
                print("------------------------------------------------------------------------")
                print()

            elif escribir_mensaje == "N" or escribir_mensaje == "n":
                continuar=False
                print()

def escribir_archivo (nombre, edad, estatura_m, estatura_cm, list_amigos, genero, n_telefonico, ciudad_vive, estado, muro):
    print()
    print(">>·Has decidido salir. Guardando perfil en", nombre + ".user")
    archivo_usuario = open("./Semana5/usuarios/"+nombre + ".user", "w")
    archivo_usuario.write(nombre + "\n")      
    archivo_usuario.write(str(edad) + "\n")
    archivo_usuario.write(str(estatura_m + estatura_cm/100) + "\n")
    archivo_usuario.write((','.join(list_amigos)) + "\n")
    archivo_usuario.write(genero + "\n")
    archivo_usuario.write(n_telefonico + "\n")
    archivo_usuario.write(ciudad_vive + "\n")
    archivo_usuario.write(estado+"\n")
    #Escribe el 'timeline' en el archivo, a continuaciÃ³n del Ãºltimo estado
    for mensaje in muro:
        archivo_usuario.write(mensaje+"\n")
    #Una vez que hemos escrito todos los datos del usuario en el archivo, no debemos olvidar cerrarlo
    archivo_usuario.close()
    print(">>·Archivo", nombre + ".user", "guardado")

#Publica el ultimo mensaje estado de cada uno de mis amigos
def ultimos_estados(list_amigos):
    print()
    print("------------------------Los ultimos estados de tus amigos-------------------")
    print("----------------------------------------------------------------------------")
    for amigo in list_amigos:
        archivo = open("./Semana5/usuarios/"+amigo+".user", "r")
        for i in range(8):
            linea = archivo.readline().rstrip()
        print(amigo+":", linea)
        archivo.close()
    print("----------------------------------------------------------------------------")
    