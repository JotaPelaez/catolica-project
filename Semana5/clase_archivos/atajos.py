""" Ctrl + enter ---> salto de linea sin importar la posicionestoy escribiendo
Alt + ↓ / ↑ --> Mueve la linea hacia arriba. Funciona con bloques tambien.
Shift + Alt + ↓ / ↑ --> Duplico la linea. Funciona con bloques tambien.
Ctrl + Shift + flecha derecha --> Selecciona palabra x palabra.
Ctrl ++ --> Agrandar tamaño de pantalla.
Ctrl + Shift + 7 ---> Para comentarios.
Shift + Alt + A ---> Para comentarios en bloque.
Ctrl + Shift + k ---> Elimina linea.
Shift + Tab ---> Elimina la indentacion.
Ctrl + B ---> Oculta la columna menu de archivos directorio
Alt + 91 ---> Abre corchete [
Alt + 93 ---> Cierra corchete ]
Alt + Shift ---> Arreglar teclado desconfigurado. Tambien Windows + barra espaciadora o tambien Shift + NumLock"""     


def leer_archivo (name):
    print("Leyendo datos de usuario", name, "desde archivo.")
    archivo_usuario = open(name+".user", "r")
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